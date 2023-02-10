# 1. Напишите программу, которая принимает на вход строку, и отслеживает,
# сколько раз каждый символ уже встречался.
# 'Hello, World!'
# H: 1
# e: 1
# l: 3
# o: 2
# W: 1
# ' ': 1  - пробел
# ,: 1
# r: 1
# d: 1
# !: 1


# our_string = 'Hello, world!'
# our_dict = {}
# count_list = set(our_string)
# for letter in count_list:
#     count_letter = 0
#     for letter_in_word in our_string:
#         if letter == letter_in_word:
#             count_letter+=1
#     our_dict[letter] = count_letter
# print(our_dict)


text = input('Введите текст: ')
d = {}
for i in text:
    d[i] = d.get(i,0)+1
print(d)


