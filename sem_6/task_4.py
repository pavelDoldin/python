# Два различных натуральных числа n и m называютсядружественными, если сумма 
# делителей числа n(включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.По данному числу k выведите 
# все пары дружественныхчисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, непревосходящее 105. 
# Программа должна вывести всепары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной встроке, разделяя пробелами. 
# Каждая пара должна бытьвыведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод:
# 300 220
# Вывод:
# 284

def delit(num: int) -> int:
    result_sum = 0
    for i in range(1, (num // 2) + 1):
        if num%i == 0:
            result_sum += i
    return result_sum

k = int(input('k: '))
result = []
for i in range(2, k + 1):
    delit_num_1 = delit(i)
    delit_num_2 = delit(delit_num_1)
    duet = {i, delit_num_1}
    if (i == delit_num_2) and (i != delit_num_1) and (duet not in result):
        result.append(duet)
print(*result)