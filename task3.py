def my_func(num1, num2, num3):

    try:
        my_list = list(map(float, [num1, num2, num3]))
        my_list.remove(min(my_list))
        return sum(my_list)
    except (TypeError,ValueError):
        return 'Вводите только цифры'
print(my_func(input('Введите первое значение: '), input('Введите второе значение: '), input('Введите третье значение: ')))
