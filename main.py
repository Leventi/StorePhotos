from vkontakte import VkPhoto
from yadisk import YandexDisk
from ok import Ok


if __name__ == '__main__':

    while True:
        social_nw = input(
            """Выберите социальную сеть:
            1. ВКонтакте [1]
            2. Одноклассники [2]
            Укажите индекс: """
        )

        if social_nw == '1':
            album = input(
                """Выберите альбом:
                1. Стена [wall] [1]
                2. Профиль [profile] [2]
                Укажите наименование или индекс: """
            )
            if album == '1' or album == 'wall':
                album = 'wall'
            else:
                album = 'profile'

            account = input('Введите имя аккаунта: ')

            photo_count = int(input(
                """Укажите количество фотографий: """
            ))

            user_vk = VkPhoto(account, album, photo_count)
            user_id_vk = user_vk.get_user_id()

            *_, photo_quantity_vk = user_vk.get_photo()
            print(f'Всего фотографий в этом разделе {photo_quantity_vk}. Вы запросили {photo_count}')

            photo_dict_vk, photo_quantity_vk = user_vk.get_photo()

            upload_vk = YandexDisk(user_id_vk, photo_dict_vk)
            upload_vk.mk_dir()

        elif social_nw == '2':
            account = input('Введите ID аккаунта: ')
            photo_count = int(input('Укажите количество фотографий: '))

            if photo_count > 100:
                while photo_count > 100:
                    photo_count = int(input(
                        """За один раз можно скачать максимум 100 фотографий
        Укажите количество фотографий: """
                    ))

            user_ok = Ok(account, photo_count)
            user_id_ok = user_ok.fid
            user_photo_ok, have_photos, totalphotos = user_ok.ok_get_photo()

            if have_photos is True:
                print('На аккаунте доступно больше фотографий чем вы указали')
            else:
                print(f'На аккаунте всего {totalphotos} фотографий. Скачиваем все.')

            upload_ok = YandexDisk(user_id_ok, user_photo_ok)
            upload_ok.mk_dir()

        else:
            listen = input(
                """Вы хотите выйти?
                1. Да [1]
                2. Нет [2]
                Укажите индекс: """
            )

            if listen == '1':
                break
            else:
                pass