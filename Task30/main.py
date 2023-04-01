# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: a
# n = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
def GetArrayArithmeticProgress(a, b, c):
    array = [a]
   
    for i in range(2, c+1):
        element = a + (i-1) * b
        array.append(element)
    return array

a1 = int(input('Введите первый элемент массива:'))
d = int(input('Введите разность:'))
n = int(input('Введите колличество элементов массива:'))
result = GetArrayArithmeticProgress(a1, d, n)

print(result)


