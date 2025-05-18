import sys
nums_path = sys.argv[-1]

with open(nums_path, encoding='utf-8') as file:
    nums = [int(i.strip()) for i in file.readlines()]

def check(num, ls):
    count = 0
    for i in ls[:]:
        if i > num:
            count += i - num
        elif i < num:
            count += num - i
    return count

print(min(check(i, nums) for i in nums))