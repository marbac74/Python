import math

def mia_radq(a):
    x = 3
    y = 0
    epsilon = 0.0000001
    while True:
        y = (x + (a / x)) / 2
        if abs(y - x) < epsilon:
            break
        x = y
    return y

print('a', '\t', 'mia_radq(a)', '\t', 'math.sqrt(a)', '\t', 'diff')
for num in [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]:
    print(round(num, 10), '\t', round(mia_radq(num), 10), '\t', round(math.sqrt(num), 10), '\t', (mia_radq(num) - math.sqrt(num)))

"""
def test_radq():
    for num in [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]:
        mia_radq(num)
"""