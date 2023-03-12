def my_func(num1, num2, num3):
    my_list = list([num1, num2, num3])
    try:
        my_list.remove(min(my_list))
        return sum(my_list)
    except (TypeError,ValueError):
        return 'Вводите только цифры'
print(my_func(int(input('Введите первое значение: ')), int(input('Введите второе значение: ')), int(input('Введите третье значение: '))))
