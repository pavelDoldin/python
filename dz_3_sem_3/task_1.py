# Требуется вычислить, сколько раз встречается некоторое число X в 
# массиве A[1..N]. Пользователь в первой строке вводит натуральное 
# число N – количество элементов в массиве. В последующих строках записаны 
# N целых чисел Ai. Последняя строка содержит число X.
# Пример
# 5
# 1 2 3 4 5
# 3
# -> 1

# знаю что не правильно, всё равно добью позже.
n = [1, 2, 3, 4, 5]
count = 0
a = int(input('Введите повторяющее число: '))
for i in n:
    if i == a:
        count += 1
for j in range(len(n)):
    print(n[j])
print()
print(a)
print()
print(count)
 

# count = 0
# n = int(input('Введите количество элементов: '))
# a = [int(input('Введите элементы: ')) for i in range(n)]
# x = int(input('Введите повторяющее число: '))
# b = [abs(a[i]==x) for i in range(len(a))]
# for j in range(len(a)):
#     print(a[j])
# print(b)