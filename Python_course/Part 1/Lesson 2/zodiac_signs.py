print('Введите месяц:')
month = input()
print('Ввеите дату:')
date = int(input())
if month == 'январь' and date < 21:
    print('Козерог')
elif month == 'январь' and date < 32 or month == 'февраль' and date < 19:
    print('Водолей')
elif month == 'февраль' and date < 30 or month == 'март' and date < 21:
    print('Рыбы')
elif month == 'март' and date < 32 or month == 'апрель' and date < 20:
    print('Овен')
elif month == 'апрель' and date < 31 or month == 'май' and date < 21:
    print('Телец')
elif month == 'май' and date < 32 or month == 'июнь' and date < 22:
    print('Близнецы')
elif month == 'июнь' and date < 31 or month == 'июль' and date < 23:
    print('Рак')
elif month == 'июль' and date < 32 or month == 'август' and date < 23:
    print('Лев')
elif month == 'август' and date < 31 or month == 'сентябрь' and date < 23:
    print('Дева')
elif month == 'сентябрь' and date < 32 or month == 'октябрь' and date < 24:
    print('Весы')
elif month == 'октябрь' and date < 31 or month == 'ноябрь' and date < 23:
    print('Скорпион')
elif month == 'ноябрь' and date < 31 or month == 'декабрь' and date < 22:
    print('Стрелец')
elif month == 'декабрь' and date < 32:
    print('Козерог')
else:
    print('Проверьте введенные данные')