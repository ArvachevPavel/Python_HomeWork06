import math
import functools
 
 
a = []
while True:
    tmp = input('Введите число: ')
    if tmp:
        a.append(int(tmp))
    else:
        break

print(f"Наименьшее общее кратное этих чисел: {functools.reduce(lambda x, y: math.gcd(x, y), a)}")