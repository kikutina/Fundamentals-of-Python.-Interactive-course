"""5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
 У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы
 с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них."""
rating_list = [9, 7, 4, 3, 2]
print(f'Результат: {rating_list}')
rating = int(input('Введите новый элемент : '))
i=0
n = len(rating_list)
while i < n:
    if rating >= rating_list[i]:
        rating_list.insert(i+1, int(rating))
        break
    i += 1
    if i==n:
        rating_list.insert(i, rating)
        break
print(f'Пользователь ввел число {rating}. Результат: {rating_list}')