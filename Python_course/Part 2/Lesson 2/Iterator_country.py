import json


class Iterator_coutry:

    def __init__(self, path):
        self.start = -1
        self.path = path
        with open('countries.json', encoding='utf8') as file:
            self.data = json.load(file)
        self.file = open(path, 'w', encoding='utf8')

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start >= len(self.data):
            self.file.close()
            raise StopIteration
        country_name = self.data[self.start]['name']['official']
        pair = country_name + ' - ' + 'https://en.wikipedia.org/wiki/' + country_name.replace(' ', '_')
        to_write = str(pair)
        self.file.write(f'{to_write}\n')


if __name__ == '__main__':
    country_list = Iterator_coutry('pair.txt')
    for item in country_list:
        next(country_list)
