# Задача 1:
# Вычислить число pi c заданной точностью d
# Пример:
# •  при $d = 0.001, π = 3.141.$

import math
def pi():
    pi = math.atan(1) * 4
    accuracy = str(input("Введите точность до 15 знака после запятой (например 0.001): "))
    value = len(accuracy[2::])
    print(round(pi, value))
pi()