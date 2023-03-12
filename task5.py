
def sum_users_list():
    users_sum = 0
    while True:
        err = False
        users_list = input('Введите числа через пробел, для выхода введите q: ').split(' ')
        for i in users_list:
            if i.lower() == 'q':
                return users_sum
            else:
                try:
                    s += sum(i)
                except ValueError:
                    err = True
        if err:
            print('Вводимое некорректно')
    print(f'Сумма введенного: {users_sum}')

