"""6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text."""

def int_func():
    a = input('Введите слова латинскими буквами через пробел: ')
    print(a.title())

int_func()
