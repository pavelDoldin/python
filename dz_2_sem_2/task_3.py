# Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8


#n = int(input('Введите число: '))


n=int(input('Введите число: '))
p=1
while p<=n:
    print(p,end=' ')
    p=p*2