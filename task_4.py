'''4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.'''

new_str = input('Введите несколько слов разделенных пробелом: ')
n = new_str.split( )
for  ind, n in enumerate (n, 1):
    if len(n)>=10:
        n=n[:10]
    print(ind, n)