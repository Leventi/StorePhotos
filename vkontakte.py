import json
import requests

VK_VER = '5.131'
VK_URL = 'https://api.vk.com/method/'

with open('vktoken.txt', 'r') as vk_token:
    VK_TOKEN = vk_token.read()


########################
#Поиск фото по имени пользователя
########################
class VkPhoto:
    def __init__(self, user_name, token=VK_TOKEN, version=VK_VER):
        self.user_name = user_name
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

    def get_photo(self):
        get_photo_url = VK_URL + 'photos.get'
        photo_params = {
            'owner_id': self.get_user_id(),
            'album_id': 'profile',
            'extended': '1',
            'photo_sizes': '1',
            'count': '5'                        #Количество загружаемых фотографий
        }
        res = requests.get(get_photo_url, params={**self.params, **photo_params}).json()

        photo_dict = {}
        vk_log_list = []
        for photo in res['response']['items']:
            photo_size = photo['sizes'][-1]['type']
            max_size_photos = photo['sizes'][-1]['url']
            photo_name = str(photo['likes']['count']) + '.jpg'

            if photo_name in photo_dict:
                photo_name = str(photo['date']) + '_' + photo_name

            photo_dict[photo_name] = max_size_photos

            json_dict = {"file_name": photo_name, "size": photo_size}
            vk_log_list.append(json_dict)

        with open('vk_photo.json', 'w', encoding='utf-8') as file:
            json.dump(vk_log_list, file, indent=2)

        return photo_dict
