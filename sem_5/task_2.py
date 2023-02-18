# Хакер Василий получил доступ к классному журналу и хочет заменить все свои
# минимальные оценки на максимальные. Напишите программу,
# которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# [4, 2, 2, 1, 5, 5]


# num = int(input('Введите num: '))
# my_list = []
# for i in range(num):
#     n = int(input('Введите n: '))
#     my_list.append(n)
# for i in range(len(my_list)):
#     if my_list[i] == 5 or my_list[i] == 4:
#         my_list[i] = 2
# print(my_list)



def replace_marks(marks_list: list) -> list:
    for i in range(len(marks_list)):
        if (marks_list[i] == 5) or (marks_list[i] == 4):
            marks_list[i] = 2
    return marks_list


marks = [4, 2, 2, 1, 5, 5]
print(replace_marks(marks))