"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""


def is_check(answer, right):
    res = answer == right
    if not res:
        print("Не верно")
    return res


year = input('Ввведите год рождения А.С.Пушкина:')
while not is_check(year, '1799'):
    year = input('Ввведите год рождения А.С.Пушкина:')

day = input('Ввведите день рождения Пушкин?')
while not is_check(day, '6'):
    day = input('В какой день июня родился Пушкин?')
print('Верно')
