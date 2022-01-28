"""Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения."""

from itertools import count
from itertools import cycle
#a)
for el in count(int(input('введите стартовое число не от 0 до 10: '))):
    if el>=11:
        break
    else:
        print(el)

#b)
new_list=["python", "java", "perl", "javascript"]

iter = cycle(new_list)
b=True
while b:
    a = input('Введите * для завершения цикла: ')
    for el in a:
        if a == "*":
            b=False
        else:
            print(next(iter))
            print(next(iter))
            print(next(iter))
            print(next(iter))