import math
a = eval(input())
b = eval(input())
c = eval(input())
if a < 0: # 使a係數為正
    a, b, c = -a, -b, -c
deter = b ** 2 - 4 * a * c
if deter > 0:
    x1 = (-b + math.sqrt(deter)) / (2 * a)
    x2 = (-b - math.sqrt(deter)) / (2 * a)
    print(round(x1, 1), round(x2, 1), sep=',')
elif deter < 0:
    real = round(-b / (2 * a), 1)
    imag = round(math.sqrt(-deter) / (2 * a), 1)
    print(str(real)+'+'+str(imag)+'i', end=',')
    print(real, '-', imag, 'i', sep='')
else:
    x = -b / (2 * a)
    print(round(x, 1))