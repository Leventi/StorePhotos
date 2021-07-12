from hashlib import md5
import requests

OK_URL = "https://api.ok.ru/fb.do"

application_key = ''
access_token = ''
session_secret_key = ''


class Ok:
    def __init__(self, fid, count):
        self.fid = fid
        self.count = count
        self.params = {
            'application_key': application_key,
            'count': self.count,
            'fid': self.fid,
            'format': 'json',
            'method': 'photos.getPhotos'
        }


    def signature(self):
        str_params = ''.join(['{}={}'.format(key, self.params[key]) for key in sorted(self.params.keys())])
        sig = md5('{}{}'.format(str_params, session_secret_key).encode('utf-8')).hexdigest().lower()

        secret_params = {
            'sig': sig,
            'access_token': access_token
        }

        self.params.update(secret_params)
        return self.params


    def ok_get_photo(self):
        res = requests.get(OK_URL, self.signature()).json()

        ok_photos = {}
        for i in res['photos']:
            photo_id = str(i['id']) + '.jpg'
            photo_size = i['pic640x480']
            ok_photos[photo_id] = photo_size

        return ok_photos

