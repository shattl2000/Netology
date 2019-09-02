import csv
import re

contacts_list = []

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    for row in rows:
        contacts_list.append(','.join(row))

# TODO 1: выполните пункты 1-3 ДЗ
finally_contact_list = []

patterns = [
    ['^(\w+)( |,)(\w+)( |,)(\w+|),(,+|)(,,,|[А-Яа-я]+)', r'\1,\3,\5,\7'],
    ['(\+7|8)\s*(\(|)(\d{3})[\s\)-]*(\d{3})\-*(\d{2})\-*(\d{2})', r'+7(\3)\4-\5-\6'],
    ['\(?доб\.\s(\d{4})\)*', r'доб.\1']
]

for contact in contacts_list:
    for pattern in patterns:
        find = re.findall(pattern[0], contact)
        contact = re.sub(pattern[0], pattern[1], contact)
    finally_contact_list.append(contact.split(','))

del_contact = []

for i in range(1, len(finally_contact_list) - 1):
    for m in range(i + 1, len(finally_contact_list)):
        if finally_contact_list[i][0] == finally_contact_list[m][0]:
            for k in range(7):
                if finally_contact_list[i][k] == '':
                    finally_contact_list[i][k] = finally_contact_list[m][k]
            del_contact.append(finally_contact_list[m])

for _ in del_contact:
    finally_contact_list.remove(_)

# TODO 2: сохраните получившиеся данные в другой файл
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(finally_contact_list)
