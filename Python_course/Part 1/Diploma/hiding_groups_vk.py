# Список групп get.groups
# Список друзей get.friends
# Искать в группе конкретного пользователя из друзей isMember
# Если друзей нет, записать имя группы в новый список
# Записать в json

from urllib.parse import urlencode
import requests

# APP_ID = "7065675"
# AUTH_URL = "https://oauth.vk.com/authorize"
# AUTH_DATA = {
#     'client_id': APP_ID,
#     'display': 'page',
#     'scope': 'friends',
#     'response_type': 'token',
# }
#
# print('?'.join((AUTH_URL, urlencode(AUTH_DATA))))

TOKEN = 'fa1c3953ab6af0bee931dfebdafa4f866c9463ce8bda433568816b14659610ffd48741eb08cc11010b3f9'


# TOKEN = '73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1'


class User:
    def __init__(self, token):
        self.token = token

    def get_params(self, user_id):
        params = {
            'access_token': self.token,
            'v': 5.92,
            'user_id': user_id,
        }
        return params

    def request(self, params, method):
        url = 'https://api.vk.com/method/{}'.format(method)
        response = requests.get(url, params=params)
        return response

    def get_groups(self, user_id):
        params = self.get_params(user_id=user_id)
        response = self.request(params=params, method='groups.get')
        groups = response.json()['response']
        return groups

    def get_friends(self, user_id):
        params = self.get_params(user_id=user_id)
        response = self.request(params=params, method='friends.get')
        friends = response.json()['response']
        return friends


print("Введите id")
user_id = input()

name = User(TOKEN)
user_group = name.get_groups(user_id)
user_friends = name.get_friends(user_id)
print("Группы", user_group)
print("Друзья", user_friends)
