# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.


def revers_nums(n):
    if n == 0:
        return ''
    k = input('--> ')
    return revers_nums(n - 1) + k

print(revers_nums(4))