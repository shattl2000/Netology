import requests
import time
import json

TOKEN = '73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1'


class User:
    def __init__(self, token):
        self.token = token

    def get_user_id(self, user):
        try:
            params = {
                'access_token': self.token,
                'v': 5.101,
                'q': user,
            }
            url = 'https://api.vk.com/method/users.search'
            response = requests.get(url, params=params).json()
            user_id = response['response']['items'][0]['id']
        except:
            user_id = user
        return user_id

    def get_params(self, user_id, group_pk=None):
        params = {
            'access_token': self.token,
            'v': 5.92,
            'group_id': group_pk,
            'user_id': user_id,
            'fields': 'members_count'
        }
        return params

    def request(self, params, method):
        url = 'https://api.vk.com/method/{}'.format(method)
        response = requests.get(url, params=params, timeout=300)
        return response

    def get_groups(self, params):
        response = self.request(
            params=params,
            method='groups.get'
        )
        return set(response.json()['response']['items'])

    def get_friends(self, params):
        response = self.request(
            params=params,
            method='friends.get'
        )
        return response.json()['response']['items']

    def get_friends_groups(self, params):
        friends_group = []
        friends = self.get_friends(params=params)
        count = len(friends)
        for friend in friends:
            time.sleep(0.3)
            response = self.request(
                params=self.get_params(user_id=friend['id']),
                method='groups.get',
            ).json()
            if 'error' in response:
                print("Осталось проверить", count - 1, "групп")
                count -= 1
                continue
            else:
                friends_group.extend(response['response']['items'])
            print("Осталось проверить", count - 1, "групп")
            count -= 1
        return set(friends_group)

    def get_only_user_groups_list(self, params):
        user_groups_set = self.get_groups(params=params)
        friend_groups_set = self.get_friends_groups(params=params)
        return user_groups_set.difference(friend_groups_set)

    def get_info_only_user_groups_list(self, params):
        groups_pk = self.get_only_user_groups_list(params)
        groups_list = []
        for group_pk in groups_pk:
            time.sleep(0.3)
            group_info_dict = {}
            group_pk_params = self.get_params(user_id=params['user_id'], group_pk=group_pk)
            response = self.request(params=group_pk_params, method='groups.getById')
            group_info_dict['name'] = response.json()['response'][0]['name']
            group_info_dict['gid'] = response.json()['response'][0]['id']
            group_info_dict['members_count'] = response.json()['response'][0]['members_count']
            groups_list.append(group_info_dict)
        return groups_list

    def write_group_list_json(self, params):
        group_list = self.get_info_only_user_groups_list(params=params)
        with open('groups.json', 'w') as f:
            f.write(json.dumps(group_list))


print("Введите id")
user = input()
name = User(TOKEN)
user_id = name.get_user_id(user)
get_params = name.get_params(user_id=user_id)
name.write_group_list_json(params=get_params)
