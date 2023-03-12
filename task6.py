def my_func():
    for word_list in input('Введите слова с маленькой буквы на латинском через пробел: \n').split(' '):
        i = 0
        for i in word_list:
            if 97 <= ord(i) <=122:
                i += 1
        print(word_list.title() if i == len(word_list) else f'{word_list} - только маленькими латинскими буквами')

