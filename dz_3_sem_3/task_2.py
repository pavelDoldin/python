# Требуется найти в массиве A[1..N] самый близкий по величине 
# элемент к заданному числу X. Пользователь в первой строке вводит 
# натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
# Пример
# 5
# 1 2 3 4 5
# 6
# -> 5


n = int(input('Кол. чисел:'))
a=[int(input('Ввести число:')) for i in range(n)]
x=int(input('Заданное число:'))
b=[abs(a[i]-x) for i in range(len(a))]
print(a[b.index(min(b))])