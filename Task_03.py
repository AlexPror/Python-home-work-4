# Задача 3. Задайте последовательность чисел. Напишите программу,
# которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

def uniqList(list):
    uniqElemList = [i for i in list if list.count(i) == 1]
    return uniqElemList

list = [1, 1, 2, 3, 4, 5, 5]
result = uniqList(list)
print(result)
