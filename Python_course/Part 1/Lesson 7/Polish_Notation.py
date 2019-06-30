print("Введите два положитеьных числа:")
string = input()
list_num = []
for element in string.split(" "):
    list_num.append(element)

operations = ["+", "-", "*", "/"]
assert list_num[0] in operations, "Первое значение не определено"

try:
    if list_num[0] == "+":
        result = int(list_num[1]) + int(list_num[2])
        print(result)
    elif list_num[0] == "-":
        result = int(list_num[1]) - int(list_num[2])
        print(result)
    elif list_num[0] == "*":
        result = int(list_num[1]) * int(list_num[2])
        print(result)
    elif list_num[0] == "/":
        result = int(list_num[1]) / int(list_num[2])
        print(result)
except ZeroDivisionError:
    print("На ноль делить нельзя")
except ValueError:
    print("Нельзя строки перевести в числа")
except IndexError:
    print("Введены не все значения")
