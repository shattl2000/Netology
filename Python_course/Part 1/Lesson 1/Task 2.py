print('Введите заработную плату:')
salary = int(input())
print('Введите сколько процентов уходит на ипотеку:')
mortgage = int(input())
print('Введите сколько процентов уходит на жизнь:')
life = int(input())
print('Введите колличество премий за год:')
prize = int(input())
full_salary = salary * 12
full_mortgage = full_salary * mortgage / 100
full_life = full_salary * life / 100
save_prize = salary / 2 * prize
residue = full_salary - (full_mortgage + full_life) + save_prize
print('На ипотеку было потрачено: ', full_mortgage, ' рублей')
print('Было накоплено: ', residue, ' рублей')