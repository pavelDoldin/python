# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8


def step(a,b):
    if b == 0:
        return 1
    if b<0:
        return 1/step(a, -b)
    if b%2 == 0:
        return step(a,b//2) * step(a,b//2)
    else:
        return step(a, b-1) * a

a = int(input('Введите число: '))
b = int(input('Введите число: '))
print(step(a,b))