import unittest
from Vkinder.vkinder import Vkinder
from mock import patch

info_user = [{'id': , 'first_name': 'Александр', 'last_name': 'Кузьмин',
              'sex': 2, 'bdate': '9.7.1988', 'city': {'id': 1, 'title': 'Москва'},
              'interests': '', 'music': '', 'books': ''}]


@patch('builtins.input', lambda *args: '22', '23')
class Test(unittest.TestCase):

    def test_is_instance_of_vkinder(self):
        vkinder = Vkinder()
        self.assertIsInstance(vkinder, Vkinder)

    def test_find_users(self):
        vkinder = Vkinder()
        self.assertIsInstance(vkinder.get_users_info(info_user), tuple)

    def test_get_raiting_users(self):
        vkinder = Vkinder()
        self.assertIsInstance(vkinder.get_raiting_users(info_user), list)

    def test_get_users_photo(self):
        vkinder = Vkinder()
        self.assertEqual(len(vkinder.get_users_photo(info_user)), 10)
