# Данно натураьное число А > 1. Определите, каким по счёту числом Фибоначчи
# Оно является, то есть выведите число n, ято ф(n)=A.
# Если А не вляется числом Фибоначчи, введите число -1.


n = int(input('Введите число: '))
f_1 = 1
f_2 = 1
num_index = 2
while f_2 < n:
    num_index += 1
    f_1, f_2 = f_2, f_1 + f_2

if f_2 == n:
    print(num_index)
else:
    print(-1)