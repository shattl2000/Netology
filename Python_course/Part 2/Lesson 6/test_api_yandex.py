import requests
import unittest


class YandexApiTest(unittest.TestCase):
    API_KEY = 'trnsl.1.1.20190711T170733Z.3323207c2ba7e432.4912d199bcdc4bb0aa2a8f5162c4f085e5d7dbb9'
    URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

    def setUp(self) -> None:
        self.session = requests.Session()

    def test_api_yandex(self):
        text = 'hello'
        params = {'key': self.API_KEY, 'lang': 'ru', 'text': text}
        response = self.session.post(self.URL, params)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['text'][0], 'привет')

    def test_api_yandex_403(self):
        text = 'hello'
        params = {'key': '123', 'lang': 'ru', 'text': text}
        response = self.session.post(self.URL, params)
        self.assertEqual(response.status_code, 403)


if __name__ == '__main__':
    unittest.main()
