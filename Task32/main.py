# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
import random

def RangeIndeces(arr,  a, b) :
    result = []    
    for i in range(len(arr)):
        
        if arr[i] > a and arr[i] < b:
            result.append(i)

    return result


lengths = int(input("Введите колличество элементов массива: "))
array = [] 
for i in range(lengths):
        array.append(random.randint(-10, 10))
print(array)

min = int(input("Задайте минимум: "))
max = int(input("Задайте максимум: "))

indexArray = RangeIndeces(array, min, max)

print(indexArray)

