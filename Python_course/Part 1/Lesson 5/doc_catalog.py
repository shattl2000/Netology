documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def people_name():
    name_list = []
    name = input("Введите номер документа: ")
    for number_of_documents in documents:
        for value in number_of_documents.values():
            if value == name:
                name_list.append(number_of_documents["name"])
    if name_list == []:
        print("Данных нет", "\n")
    else:
        print("Документ приндалежит:", *name_list, "\n")


def documents_list():
    for list_of_men in documents:
        e = list(list_of_men.values())
        print(e[0], str(e[1]), e[2])


def num_derictories():
    direct_list = []
    s = input("Введите номер документа: ")
    for key, value in directories.items():
        if s in value:
            direct_list.append(key)
    if direct_list == []:
        print("Документ не найден", "\n")
    else:
        print("Номер полки:", *direct_list, "\n")


def add_person():
    new_person = {"type": "", "number": "", "name": ""}
    new_person["name"] = input("Введите имя: ")
    new_person["type"] = input("Введите тип документа: ")
    type_doc = input("Введите номер документа: ")
    new_person["number"] = type_doc
    number_of_direct = input("Введите номер полки: ")
    if int(number_of_direct) > len(directories):
        print("Такой полки не существует")
    else:
        list_of_direct = directories[number_of_direct]
        list_of_direct.append(type_doc)
        documents.append(new_person)
        print(directories)
        print(documents)


def del_documents():
    del_doc = "Документ не найден"
    num_doc = input("Введите номер документа:")
    for number_of_documents in documents:
        for value in number_of_documents.values():
            if value == num_doc:
                number_of_documents["number"] = ""
                del_doc = "Документ найден и удален"
                print(documents)

    for key, value in directories.items():
        if num_doc in value:
            value.remove(num_doc)
            print(directories)
    print(del_doc)


def move_directories():
    info = "Такого документа не существует"
    num_doc = input("Введите номер документа:")
    num_directories = int(input("Введите целевую полку:"))
    if num_directories > len(directories):
        print("Такой полки нет")
        info = ""
    else:
        for key, value in directories.items():
            if num_doc in value:
                value.remove(num_doc)
                num_directories = str(num_directories)
                list_of_direct = directories[num_directories]
                list_of_direct.append(num_doc)
                info = "Документ перемещен"
        print(directories)
    print(info)


def add_shelf():
    num_new_direct = input("Введите номер новой полки:")
    if num_new_direct in directories.keys():
        print("Такая полка уже существует")
    else:
        directories[num_new_direct] = []
        print(directories)


def main():
    while True:
        print("Введите команду: ", "\n""p,", "l,", "s,", "a,", "d,", "m,", "as или", "q - выход")
        user_input = input()
        if user_input == 'p':
            people_name()
        elif user_input == 'l':
            documents_list()
        elif user_input == 's':
            num_derictories()
        elif user_input == 'a':
            add_person()
        elif user_input == 'd':
            del_documents()
        elif user_input == 'm':
            move_directories()
        elif user_input == 'as':
            add_shelf()
        elif user_input == 'q':
            print('Выход')
            break


if __name__ == "__main__":
    main()
