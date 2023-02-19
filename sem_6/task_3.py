# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод:
# 1 2 3 2 3 2
# Вывод:
# 2
# Ввод:
# 1 1 2 3 1 2
# Вывод:
# 4


def list_init(el_count: int):
    result_list = []
    for i in range(el_count):
        num = int(input('num: '))
        result_list.append(num)
    return result_list

n = int(input('n --> '))
our_list = list_init(n)
print(our_list)

count = 0
for i in range(len(our_list)-1):
    for j in range(i+1, len(our_list)):
        if our_list[j] == our_list[i]:
            count=+ 1
print(count)
