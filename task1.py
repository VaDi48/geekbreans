users_num = int(input('Введите числитель: '))
users_den = int(input('Введите знаменатель: '))

def devision_users_num(num1, num2):
    result = num1/num2
    if num2 == 0:
        print('Делить на ноль нельзя')
    else:
        print(result)
print(devision_users_num(users_num, users_den))
