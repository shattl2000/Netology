import vk_api
import json
from Vkinder.db import insert_to_db
import random

TOKEN = '407123a47938117291359f8c2f07e5a7604e35e75248abe112bc33d3838b7bfd868ce2c11f448ea99548d'

vk_session = vk_api.VkApi(token=TOKEN)

try:
    vk_session.auth(token_only=True)
except vk_api.AuthError as error_msg:
    print(error_msg)


class Vkinder:

    def get_params(
            self,
            user_id=None,
            sex=None,
            age_from=None,
            age_to=None,
            has_photo=1,
            count=1000,
            city=None
    ):
        return {
            'access_token': TOKEN,
            'user_id': user_id,
            'sex': sex,
            'age_from': age_from,
            'age_to': age_to,
            'has_photo': has_photo,
            'fields': 'interests, music, books, sex, city, bdate',
            'count': count,
            'v': '5.52',
            'city': city
        }

    def VkRequestsPool(self, method, params):
        self.method = method
        self.params = params
        with vk_api.VkRequestsPool(vk_session) as pool:
            return pool.method(method, params)

    def get_user_info(self, user_id):
        user_info = self.VkRequestsPool('users.get', self.get_params(user_id))
        return user_info

    def get_users_info(self, user):
        user_sex = user[0]['sex']
        user_bdate = int(user[0]['bdate'][-2:])
        user_music = set(user[0]['music'].split(','))
        user_books = set(user[0]['books'].split(','))
        city = user[0]['city']['id']
        print('Введите возраст')
        age_from = int(input('От: '))
        age_to = int(input('До: '))
        if user_sex == 1:
            sex = 0
        else:
            sex = 1
        params = self.get_params(sex=sex, age_from=age_from, age_to=age_to, has_photo=1, city=city)
        user_search = self.VkRequestsPool('users.search', params)

        return user_search.result, user_bdate, user_music, user_books

    @staticmethod
    def get_increment_raiting(search_user: dict, interest: str, user_interest: set,
                              raiting_incr: int) -> int:
        search_friend_interests = set(search_user[interest].split(','))
        diff_interest = user_interest - search_friend_interests
        if len(diff_interest) < len(user_interest):
            return raiting_incr
        else:
            return 0

    def get_raiting_users(self, user):
        users, user_bdate, user_music, user_books = self.get_users_info(user)
        rating_list = []
        for search_user in users['items']:
            raiting = 0
            try:
                search_user_bdate = int(search_user['bdate'][-2:])
                if search_user_bdate == user_bdate:
                    raiting += 5
                else:
                    raiting += 0
                raiting += self.get_increment_raiting(user[0], 'music', user_music, 3)
                raiting += self.get_increment_raiting(user[0], 'books', user_books, 2)
            except Exception:
                raiting += 0
            if raiting >= 5:
                search_user_dict = {search_user['id']: raiting}
                rating_list.append(search_user_dict)
        return rating_list

    def get_users_photo(self, user):
        raiting_list = self.get_raiting_users(user)
        random_top10 = random.sample(raiting_list, 10)
        sorted_users = []
        for user in random_top10:
            params = {'owner_id': int(*user.keys()),
                      'access_token': TOKEN,
                      'album_id': 'profile',
                      'extended': 1}
            with vk_api.VkRequestsPool(vk_session) as pool:
                photos = pool.method('photos.get', params)
            photos = photos.result
            top_3_photo = []
            for photo in photos['items']:
                top_3_photo.append({
                    'id': photo['id'],
                    'likes': photo['likes']['count']
                })
            top_3_photo.sort(key=lambda dict: dict['likes'], reverse=True)
            top_3_photo = top_3_photo[0:3]
            sorted_users.append({
                'user_id': int(*user.keys()),
                'likes': top_3_photo
            })
        print(sorted_users)
        return sorted_users

    def write_top10users_json(self, sorted_users):
        with open('data/top10users.json', 'w', encoding='utf-8') as file:
            json.dump(sorted_users, file, ensure_ascii=False, indent=2)
        with open('data/top10users.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def insert_db(self, sorted_users):
        for user in sorted_users:
            for photo in user.get('likes'):
                photo_id = photo['id']
                photo_likes = photo['likes']
                insert_to_db(user['user_id'], photo_id, photo_likes)


if __name__ == '__main__':
    user_id = int(input('Введите ваш id: '))
    vk_kinder = Vkinder()
    info = vk_kinder.get_user_info(user_id=user_id)
    users = vk_kinder.get_users_photo(user=info.result)
    vk_kinder.write_top10users_json(sorted_users=users)
    vk_kinder.insert_db(sorted_users=users)
