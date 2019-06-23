# Проверка на возраст призывника;
#Количество детей;
#Учится ли он сейчас.

height = 175
age = 18
children = 3
student = "yes" 

if height < 170:
    print('Будет танкистом')
elif height < 185:
    print('Пойдет на флот')
elif height < 200:
    print('Пойдешь в десантники')
else:
    print('Слишком длинный')

if 17 < age < 28 and children < 3 and student == "no":
    print('Годен')
else:
    print('Военкомату ты пока не интересен')