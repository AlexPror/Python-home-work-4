# Задача 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

import re

with open('C:/Users/lenovo/Home work 4/file_result.txt', 'r') as file:
    string1 = file.read()
    #print(list1)
with open('C:/Users/lenovo/Home work 4/file_result2.txt', 'r') as file:
    string2 = file.read()

numbers = re.findall(r'\d+', string1)
numbers = [int(i) for i in numbers]
print(numbers)
value2 = numbers[::2]
print(value2)