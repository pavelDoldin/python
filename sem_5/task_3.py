# Напишите функцию, которая принимает одно число и проверяет, 
# является ли оно простым


n = int(input("Введите число: "))
def test(num):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(test(n))


# def natural_num(num):
#     for i in range(2, num):
#         if num % i == 0:
#             return True   # истина
#     return False          # ложь



# number = int(input('Введите число: '))
# print(natural_num(number))