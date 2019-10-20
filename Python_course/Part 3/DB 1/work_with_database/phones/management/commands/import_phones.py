import csv
from django.utils.text import slugify

from django.core.management.base import BaseCommand
# from phones.models import Phone
from ...models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)

            for line in phone_reader:
                phone = Phone()
                phone.id = line[0]
                phone.name = line[1]
                phone.image = line[2]
                phone.price = line[3]
                phone.release_date = line[4]
                phone.lte_exists = line[5]
                phone.save()
