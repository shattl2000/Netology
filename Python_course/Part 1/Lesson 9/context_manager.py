from contextlib import contextmanager
import datetime


@contextmanager
def file_open(path):
    try:
        f = open(path, 'w', encoding="utf-8")
        yield f
    except OSError:
        print("Ошибка")
    finally:
        f.close()
        print('Файл закрыт')


if __name__ == '__main__':
    with file_open('result.txt') as f:
        start_code = datetime.datetime.now()


        def mid_num(a):
            result = sum(a) / len(a)
            f.write("Среднее значение: ")
            f.write(str(result))


        mid_num(range(100000000))
        finish_code = datetime.datetime.now()

        dif_in_time = finish_code - start_code

        print("Код был запущен в:", start_code, '\n' "Закончен в:", finish_code,
              '\n' "Время выполнения кода составила:", dif_in_time)
