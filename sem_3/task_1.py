# Дан список чисел. Определит, сколько в нём встречается 
# различных чисел [1, 1, 2, 3, 4, 4] --> 4


my_list = [1, 1, 2, 3, 4, 4]
my_list1 = set(my_list)
print(my_list)
print(f'уникальных элементов: {len(my_list1)}')