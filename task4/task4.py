# Задание №4 Чистое
# nums = [1, 2, 3]
# nums = [1, 10, 2, 9]
with open('nums.txt', encoding='utf-8') as file:
    nums = [int(i.strip()) for i in file.readlines()]
    # print(nums)

def chek(num, ls):
    count = 0
    # print(num, '- num')
    # print()
    for i in ls[:]:
        if i > num:
            # print(i - num)
            count += i - num
        elif i < num:
            # print(num - i)
            count += num - i
    # print(count, '- count')
    return count

print(min(chek(i, nums) for i in nums))