"""2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой."""

def my_f(name, surname, year_of_birth, city, email, phone_num):
    print(f'{name} {surname}, {year_of_birth} года рождения, г. {city}, е-почта {email}, тел: {phone_num}')
a = input('Ваше имя: ')
b = input('Ваша фамилия: ')
c = input('Ваш год рождения: ')
e = input('Ваш город: ')
f = input('email: ')
g = input('номер телефона: ')
my_f(name=a, surname = b, year_of_birth=c, city= e, email= f, phone_num=g)