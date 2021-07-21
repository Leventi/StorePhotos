import json
import requests
import time

VK_VER = '5.131'
VK_URL = 'https://api.vk.com/method/'

with open('vktoken.txt', 'r') as vk_token:
    VK_TOKEN = vk_token.read()


class VkPhoto:
    def __init__(self, user_name, album='profile', count=10, token=VK_TOKEN, version=VK_VER):
        self.user_name = user_name
        self.album = album
        self.count = count
        self.params = {
            'access_token': token,
            'v': version
        }

    def get_user_id(self):
        user_id_url = VK_URL + 'users.get'
        user_params = {
            'user_ids': self.user_name
        }
        res = requests.get(user_id_url, params={**self.params, **user_params}).json()
        user_id = res['response'][0]['id']
        return user_id

    def get_photo(self) -> tuple:
        photo_dict = {}
        vk_log_list = []

        get_photo_url = VK_URL + 'photos.get'
        photo_params = {
            'owner_id': self.get_user_id(),
            'album_id': self.album,
            'extended': '1',
            'photo_sizes': '1',
            'count': self.count
        }
        res = requests.get(get_photo_url, params={**self.params, **photo_params}).json()

        try:
            photo_quantity = res['response']['count']
        except KeyError:
            print(f'У пользователя {self.user_name} нет указанного количетсва фотографий в альбоме {self.album}')
        time.sleep(0.2)

        if self.count > 1000:
            iterations = int(self.count / 1000) + 1

            for i in range(0, iterations, 1):
                photo_params['offset'] = 1000 * i
                if i == iterations-1:
                    photo_params['count'] -= 1000 * i

                res = requests.get(get_photo_url, params={**self.params, **photo_params}).json()
                time.sleep(0.2)


                for photo in res['response']['items']:
                    photo_size = photo['sizes'][-1]['type']
                    max_size_photos = photo['sizes'][-1]['url']
                    photo_name = str(photo['likes']['count']) + '.jpg'

                    if photo_name in photo_dict:
                        photo_name = str(photo['date']) + '_' + photo_name

                    photo_dict[photo_name] = max_size_photos

                    json_dict = {"file_name": photo_name, "size": photo_size}
                    vk_log_list.append(json_dict)

                photo_dict.update(photo_dict)

                with open('vk_photo.json', 'w', encoding='utf-8') as file:
                    json.dump(vk_log_list, file, indent=2)

        else:
            for photo in res['response']['items']:
                photo_size = photo['sizes'][-1]['type']
                max_size_photos = photo['sizes'][-1]['url']
                photo_name = str(photo['likes']['count']) + '.jpg'

                if photo_name in photo_dict:
                    photo_name = str(photo['date']) + '_' + photo_name

                photo_dict[photo_name] = max_size_photos

                json_dict = {"file_name": photo_name, "size": photo_size}
                vk_log_list.append(json_dict)

            photo_dict.update(photo_dict)

            with open('vk_photo.json', 'w', encoding='utf-8') as file:
                json.dump(vk_log_list, file, indent=2)

        return photo_dict, photo_quantity

