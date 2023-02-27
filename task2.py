user_num = (input('Введите значиения через пробел: '))
user_list = user_num.split(' ')
i = 0
k = 1
while k < len(user_list):
    user_list[i], user_list[k] = user_list[k], user_list[i]
    i += 2
    k += 2
    print(user_list)
