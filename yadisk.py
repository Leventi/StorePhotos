from settings import YA_TOKEN
import requests
import time
from tqdm import tqdm

YA_URL = 'https://cloud-api.yandex.net'


########################
#Выгрузка файлов на диск
########################
class YandexDisk:
    def __init__(self, user_id, get_photo):
        self.user_id = user_id
        self.get_photo = get_photo

    def get_header(self, api_key=YA_TOKEN):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {api_key}'
        }

    def mk_dir(self):
        dir_url = f'{YA_URL}/v1/disk/resources'
        headers = self.get_header()
        params = {'path': self.user_id, 'overwrite': 'true'}
        response = requests.put(dir_url, headers=headers, params=params)
        if response.status_code == 409:
            print(f'Папка {self.user_id} уже существует.')
            self.ya_file_upload()
        elif response.status_code == 201:
            print(f'Директория {self.user_id} успешно создана')
            self.ya_file_upload()
        else:
            print('Что-то пошло не так при создании папки')
        return response

    def ya_file_upload(self):
        ya_url = f'{YA_URL}/v1/disk/resources/upload'
        headers = self.get_header()

        for k, v in tqdm(self.get_photo.items()):
            params = {
                'path': f'{str(self.user_id)}/{k}',
                'url': v
            }
            response = requests.post(url=ya_url, headers=headers, params=params)
            response.raise_for_status()
            if response.status_code != 202:
                print('Что-то пошло не так при записи файлов')
            time.sleep(1)

