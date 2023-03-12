user_num = input('Введите значение числителя: ')
user_den = input('Введите значение знаменателя: ')
def division_users_num(num, den):
    try:
        num, den = int(num), int(den)
        div_users_num = num / den
    except ValueError:
        return 'Value Error'
    except ZeroDivisionError:
        return "На ноль делить нельзя!"
    return div_users_num
print(division_users_num(user_num, user_den))
