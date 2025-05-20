# Задание №1 чистое
import sys

n, m = map(int, sys.argv[1:])

if n < 1 or m < 1:
    raise Exception('Введенные цифры должны быть только положительными')
# print('работаем дальше')
if m == 0:
    print('Путь отсутствует.')
else:
    if m > n:
        m %= n
        if m == 0:
            m = n

    ls_nums = [i for i in range(1, n + 1)]
    ls_cop_nums = ls_nums[:]
    ls_inter = [ls_nums[:m]]

    while ls_inter[-1][-1] != 1:
        del ls_nums[:m - 1]
        ls_nums += ls_cop_nums
        ls_inter.append(ls_nums[:m])
    res = ''.join([str(i[0]) for i in ls_inter])
    print(res)


