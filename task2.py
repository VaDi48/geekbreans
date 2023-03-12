def users_info(**kwargs):
     return ' '.join(**kwargs.values())

print(users_info(name = input('Введите свое имя: '), surname = input(' Введите свою фамилию: '), city = input('Введите город проживания: '), phone = input(' Введите номер телефона: '), year = input('Введите год рождения: ')))