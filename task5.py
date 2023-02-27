my_list = []
users_num = int(input('Put the num: '))
if len(my_list) == 0:
    my_list.append(users_num)
elif my_list[0] < users_num:
    my_list.index(0, users_num)
elif my_list[-1] >= users_num:
    my_list.insert(len(my_list) + 1, users_num)
else:
    for i in range(len(my_list)):
        if my_list[i] < users_num:
            my_list.insert(i - 1, users_num)
print(my_list)