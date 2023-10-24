import math

def mia_radq(num):
    x = 5
    epsilon = 0.0000001
    while True:
        y = (x + num / x) / 2
        if abs(y - x) < epsilon:
            break
        x = y
    return x

print('n  \t', 'mia_radq(n)\t', 'math.sqrt(n)\t', 'diff')
for int in range(1, 10):
    print(int, '\t', round(mia_radq(int), 8), '\t', round(math.sqrt(int), 8), '\t', round(mia_radq(int) - math.sqrt(int), 8))