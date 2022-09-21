# Задача 4. Задана натуральная степень k. Сформировать случайным
# образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
#
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

def pol(k):
    newPol = ''
    for i in range(0, k+1):
        digit = randint(1, 100)
        if k == 0:
            polynomial = (f'{digit} = 0')
        elif k == 1:
            polynomial = (f'{digit}x + ')
        else:
            polynomial = (f'{digit}x^{k} + ')
        newPol += polynomial
        k -= 1
    return newPol

k = int(input('Введите натуральное число степени:'))
result = pol(k)
print(result)

# Вариант 2. В случае выпадания НУЛЯ.
# from random import randint
#
# def pol(k):
#     newPol = ''
#     for i in range(0, k+1):
#         digit = randint(0, 2)
#         if k == 0:
#             polynomial = (f'{digit} = 0')
#         elif k == 1:
#             polynomial = (f'{digit}x + ')
#         else:
#             polynomial = (f'{digit}x^{k} + ')
#         newPol = newPol + polynomial
#         k -= 1
#     return  newPol
#
# def delZero(newPol):
#     newPol = ' '.join([w for w in newPol.split() if not "0x" in w])
#     newPol = ' '.join([w for w in newPol.split() if not "0" in w])
#     newPol = ' '.join([w for w in newPol.split() if not "+" in w])
#     newPol = newPol.split()
#     return newPol
#
# def enterPlus(newPol):
#     for i in range(1, (len(newPol) - 2) * 2):
#         if i % 2 != 0:
#             newPol.insert(i, '+')
#     newPol.append("0")
#     return newPol
#
# k = int(input('Введите натуральное число степени:'))
# firstPol = pol(k)
# print(firstPol)
# delZero = delZero(firstPol)
# print(delZero)
# result = enterPlus(delZero)
# result = str(result)
# print(result)

with open('C:/Users/lenovo/Home work 4/file_result.txt', 'w') as file:
    file.writelines(f'{result}\n')