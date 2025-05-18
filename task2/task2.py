# Задание №2 выполнено
import sys
file1_path, file2_path = sys.argv[1:]

with open(file1_path, encoding='utf-8') as file1:
    x, y = map(float, file1.readline().split())
    radius = float(file1.readline())


with open(file2_path, encoding='utf_8') as file2:
    points_ls = [tuple(map(float, i.split())) for i in file2 if i.strip()]
    # print(points_ls)

for x_, y_ in points_ls:
    dist_sq = (x_ - x) ** 2 + (y_ - y) ** 2
    r_sq = radius ** 2
    if abs(dist_sq - r_sq) < 1e-6:
        print(0)
    elif dist_sq < r_sq:
        print(1)
    elif dist_sq > r_sq:
        print(2)

