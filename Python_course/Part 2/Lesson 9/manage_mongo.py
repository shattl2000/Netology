import csv
import re
from pymongo import MongoClient
from datetime import datetime

client = MongoClient()
artists_db = client['artists']
concert_collection = artists_db['concerts']


def read_data(csv_file, db):
    with open(csv_file, encoding='utf-8') as csvfile:
        artists_list = []
        reader = csv.DictReader(csvfile)
        for row in reader:
            row = dict(row)
            row['Цена'] = int(row['Цена'])
            row['Дата'] += '.2019'
            row['Дата'] = datetime.strptime(row['Дата'], '%d.%m.%Y')
            artists_list.append(row)
        print(artists_list)
        db.insert_many(artists_list)


def find_cheapest(db):
    sorted_list = list(db.find().sort('Цена', 1))
    for item in sorted_list:
        print(f'{item["Исполнитель"]}, {item["Цена"]} рублей,'
              f' {item["Место"]}, {item["Дата"]}')


def find_by_name(name, db):
    name = re.escape(name)
    regex = re.compile(name)
    sorted_list = list(db.find({'Исполнитель': regex}).sort('Цена', 1))
    print(f'Найдено мероприятий: {len(sorted_list)}')
    for item in sorted_list:
        print(f'{item["Исполнитель"]}, {item["Цена"]} рублей,'
              f' {item["Место"]}, {item["Дата"]}')


def find_by_date_range(start_date, end_date, db):
    start_date = datetime.strptime(start_date, '%d.%m.%Y')
    end_date = datetime.strptime(end_date, '%d.%m.%Y')
    sorted_list = list(db.find({'Дата': {'$gt': start_date, '$lt': end_date}}))
    print(f'Найдено концертов: {len(sorted_list)}')
    for item in sorted_list:
        print(f'{item["Исполнитель"]}, {item["Цена"]} рублей,'
              f' {item["Место"]}, {item["Дата"]}')


if __name__ == '__main__':
    read_data('artists.csv', concert_collection)
    find_cheapest(concert_collection)
    find_by_name('Ар', concert_collection)
    find_by_date_range('01.05.2019', '30.12.2019', concert_collection)
