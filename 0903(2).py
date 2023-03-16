from math import sin, cos, exp

def f(x,y):
    if x + y != 0:
        return (sin(x + y) + 2 * cos(x+y))/(x + y)
    return exp(x/2) + exp(y)

def num_point(start, stop, step):
    return round((stop - start)/step) + 1

a = 1
b = 5
hx = 1
c = -3
d = 1
hy = 0.5

print(r" y\x ", end="|")

for i in range(num_point(a, b, hx)):
    x = a + i * hx
    print(f"{x:^8}", end="")
print()
print('-'*(8*(num_point(a, b, hx))+6))
for j in range(num_point(c, d, hy)):
    y = c + j * hy
    print(f"{y:^5}|", end="")
    for i in range(num_point(a, b, hx)):
        print(f"{round(f(x,y), 3):^8}", end="")
    print()
