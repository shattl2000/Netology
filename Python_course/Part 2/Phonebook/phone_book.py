class Contact():
    def __init__(self, name, surname, phone_number, *args, favorite_contact=False, **kwargs):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.favorite_contact = favorite_contact
        self.args = args
        self.kwargs = kwargs

    def __str__(self):
        ret_str = ''
        print('Имя:', self.name)
        print('Фамилия:', self.surname)
        print('Телефонный номер:', self.phone_number)
        if self.favorite_contact:
            print('В избранных: да')
        else:
            print('В избранных: нет')
        print('Дополнительная информация:')
        for additional in self.args:
            print(f'         {additional}')
        for add_info_name, add_info_value in self.kwargs.items():
            print(f'         {add_info_name} - {add_info_value}')
        return ret_str


class PhoneBook():
    def __init__(self, name):
        self.name = name
        self.book = []

    def show_contacts(self):
        for contact in self.book:
            print(contact)

    def add_contact(self, contact):
        self.book.append(contact)

    def remove_contact(self, number):
        for contact in self.book:
            if contact.phone_number == number:
                self.book.remove(contact)

    def search_favorite_contact(self):
        for contact in self.book:
            if contact.favorite_contact:
                print(contact)

    def search_contact(self, name, surname):
        found_contacts = []
        for contact in self.book:
            if name == contact.name and surname == contact.surname:
                found_contacts.append(contact)
        if len(found_contacts) == 0:
            print('Контакта нет')
        else:
            print(*found_contacts)


jhon = Contact('Jhon', 'Smith', '+71234567809', 'PC_gaming', 'basketball', telegram='@jhony', email='jhony@smith.com')
# print(jhon)

petya = Contact('Petya', 'Ivanov', '123', favorite_contact=True, telegram='@petrukha', email='petya@ivanov.com')
# print(petya)

phone_book = PhoneBook('my_book')

phone_book.add_contact(jhon)
phone_book.add_contact(petya)

phone_book.show_contacts()

phone_book.search_favorite_contact()

phone_book.search_contact('Jhon', 'Smith')

phone_book.remove_contact('123')