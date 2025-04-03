# Задание №2 выполнено
def read_circle(file_):
    with open(file_, encoding='utf-8') as file:
        x, y = map(float, file.readline().split())
        r = float(file.readline())
        # print(x, y, r)
    return x, y, r
# read_circle('param.txt')
def read_points(file_):
    with open(file_, encoding='utf_8') as file:
        points = [tuple(map(float, line.split())) for line in file if line.strip()]
        # print(points)
    return points
# read_points('points.txt')
def position(x0, y0, r, x, y):
    dist_sq = (x - x0)**2 + (y - y0)**2
    r_sq = r**2
    if abs(dist_sq - r_sq) < 1e-6:
        return 0
    return 1 if dist_sq < r_sq else 2

def main():
    x0, y0, r = read_circle('param.txt')
    points = read_points('points.txt')
    for x, y in points:
        print(position(x0, y0, r, x, y))

main()