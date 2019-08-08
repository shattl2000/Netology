import hashlib


def generator_md5(path):
    with open(path, encoding='utf8') as file:
        file = file.readlines()

    for string in file:
        yield hashlib.md5(string.splitlines()[0].encode()).hexdigest()


for i in generator_md5('pair.txt'):
    print(i)
