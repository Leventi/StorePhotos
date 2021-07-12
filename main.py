from vkontakte import VkPhoto
from yadisk import YandexDisk
from ok import Ok

if __name__ == '__main__':

    # Выгрузка фото из ВКонтакте
    # user = VkPhoto('begemot_korovin')
    # get_user_id = user.get_user_id()
    # get_user_photo = user.get_photo()
    #
    # upload_vk = YandexDisk(get_user_id, get_user_photo)
    # upload_vk.mk_dir()

    get_photo = Ok('568710368927', '6')
    get_user_id_ok = get_photo.fid
    get_user_photo_ok = get_photo.ok_get_photo()

    upload_ok = YandexDisk(get_user_id_ok, get_user_photo_ok)
    upload_ok.mk_dir()
