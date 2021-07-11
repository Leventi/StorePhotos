from vkontakte import VkPhoto
from yadisk import YandexDisk

if __name__ == '__main__':

    user = VkPhoto('begemot_korovin')
    get_user_id = user.get_user_id()
    get_user_photo = user.get_photo()

    upload = YandexDisk(get_user_id, get_user_photo)
    upload.mk_dir()