import requests

TOKEN = "c8229dec0f558214b24b3cfb3ff193a11836be51e3bd777b9b5de6a20240ef7bb44abe6e6d204ab7ad738"


class User:
    def __init__(self, token):
        self.token = token

    def get_params(self, target_uid, source_uid):
        return {
            'access_token': self.token,
            'v': '5.52',
            'source_uid': target_uid,
            'target_uid': source_uid,
        }

    def request(self, method, params):
        response = requests.get(
            'https://api.vk.com/method/' + method,
            params=params
        )
        return response

    def mutual_friends(self, target_uid, source_uid):
        params = self.get_params(target_uid, source_uid)
        response = self.request(
            'friends.getMutual',
            params=params
        )
        return response.json()['response']


alexandr = User(TOKEN)
friends = alexandr.mutual_friends(source_uid=5211684, target_uid=1563186)
print(friends)
