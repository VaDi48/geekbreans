words = input('Put the words: ')
words_new = words.split(' ')
dict_1 = dict()
k = 1
for l in words_new:
    dict_1[k] = l
    k += 1
for k in dict_1:
    print(k, dict_1[k])
