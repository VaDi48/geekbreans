users_x = int(input('Введите число, возводимое в степень: '))
users_y = int(input('Введите степень: '))
def users_expon(x, y):
    try:
        res = x**y
        return res
    except (TypeError, ValueError):
        return 'Вводите только числа!'
print(users_expon(users_x, users_y))