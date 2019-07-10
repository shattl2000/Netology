import requests

API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_it(in_dir, out_dir, from_lang=None, to_lang='ru'):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param to_lang:
    :return:
    """
    from os import listdir
    input_dir = in_dir
    files = listdir(input_dir)
    mytxt = filter(lambda x: x.endswith('.txt'), files)

    for name_file_read in mytxt:
        full_name_file_read = in_dir + name_file_read
        with open(full_name_file_read, encoding='utf-8') as file:
            text = file.read()

        params = {
            'key': API_KEY,
            'text': text,
            'lang': '{}-{}'.format(from_lang, to_lang),
        }

        response = requests.get(URL, params=params)
        json_ = response.json()
        output_text = ''.join(json_['text'])

        name_file_write = 'result_translate.txt'
        full_name_file_write = out_dir + name_file_write

        with open(full_name_file_write, 'w', encoding='utf-8') as trans_file:
            trans_file.write(output_text)
        return output_text


translate_it('C:\\Netology\\Python_course\\Part 1\\Lesson 11\\ES\\',
             'C:\\Netology\\Python_course\\Part 1\\Lesson 11\\', 'es')
