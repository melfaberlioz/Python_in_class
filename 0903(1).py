import math

a = 0
b = 1
h = 0.1
def f(x):
    return x * math.sin(x)

n = round((b-a)/h) + 1
print('|   x   |  f(x)  |')
print('-'*18)
for i in range(n):
    x = a + h * i
    y = f(x)
    print(f"|{round(x, 4):^7}|{round(y, 4):^8}|")
