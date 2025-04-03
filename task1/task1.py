# Задание №1 чистое
n, m = map(int, input().split())
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
    # print(ls_inter)

    while ls_inter[-1][-1] != 1:
        del ls_nums[:m - 1]
        ls_nums += ls_cop_nums
        ls_inter.append(ls_nums[:m])
        # print(ls_nums)
        # break
    # print(ls_inter)
    res = ''.join([str(i[0]) for i in ls_inter])
    print(res)