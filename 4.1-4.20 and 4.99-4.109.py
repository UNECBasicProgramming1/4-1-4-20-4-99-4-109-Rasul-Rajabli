import math
# 4.1
a = float(input())
b = float(input())
print("Большее:", max(a, b))
print("Меньшее:", min(a, b))

# 4.2
x = float(input())
if x > 0:
    y = math.sin(x) ** 2
else:
    y = 1 - 2 * math.sin(x ** 2)
print(y)

# 4.3
x = float(input())
if x > 0:
    y = math.sin(x ** 2)
else:
    y = 1 + 2 * math.sin(x ** 2)
print(y)

# 4.4
x = float(input())
y = float(input())
if x < 4:
    print("I")
else:
    print("II")

# 4.5
x = float(input())
y = float(input())
if y > 3:
    print("I")
else:
    print("II")

# 4.6 (а)
x = float(input())
if x < 2:
    y = x
else:
    y = 2
print(y)

# 4.6 (б)
x = float(input())
if x < 3:
    y = -x
else:
    y = -3
print(y)

# 4.7
x = float(input())
if math.sin(x) < 0:
    k = x ** 2
else:
    k = abs(x)
if k < x:
    f = k * x
else:
    f = k + x
print(f)

# 4.8
x = float(input())
if math.sin(x) >= 0:
    k = x ** 2
else:
    k = abs(x)
if x < k:
    f = abs(x)
else:
    f = k * x
print(f)

# 4.9
a = float(input())
b = float(input())
print("max =", a if a > b else b)
print("min =", a if a < b else b)

# 4.10
km = float(input())
ft = float(input())
m1 = km * 1000
m2 = ft * 0.3048
if m1 < m2:
    print("Меньше километры")
else:
    print("Меньше футы")

# 4.11
a = float(input())
b = float(input())
if a / 3.6 > b:
    print("Первая")
elif a / 3.6 < b:
    print("Вторая")
else:
    print("Равны")

# 4.12
r = float(input())
s = float(input())
a1 = math.pi * r * r
a2 = s * s
if a1 > a2:
    print("Круг")
elif a1 < a2:
    print("Квадрат")
else:
    print("Равны")

# 4.13
v1 = float(input())
m1 = float(input())
v2 = float(input())
m2 = float(input())
d1 = m1 / v1
d2 = m2 / v2
if d1 > d2:
    print("Первый")
elif d1 < d2:
    print("Второй")
else:
    print("Одинаковые")

# 4.14
r1 = float(input())
u1 = float(input())
r2 = float(input())
u2 = float(input())
i1 = u1 / r1
i2 = u2 / r2
if i1 < i2:
    print("Первый")
elif i1 > i2:
    print("Второй")
else:
    print("Токи равны")

# 4.15
a = float(input())
b = float(input())
c = float(input())
d = b*b - 4*a*c
if d >= 0:
    print("Корни есть")
else:
    print("Корней нет")

# 4.16
a = float(input())
b = float(input())
c = float(input())
d = b*b - 4*a*c
if d < 0:
    print("Корней нет")
else:
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    print(x1)
    print(x2)

# 4.17
yb = int(input())
mb = int(input())
yc = int(input())
mc = int(input())
age = yc - yb
if mc < mb:
    age -= 1
print(age)

# 4.18
s_circle = float(input())
s_square = float(input())
r = math.sqrt(s_circle / math.pi)
d = 2 * r
a = math.sqrt(s_square)
if d <= a:
    print("Да")
else:
    print("Нет")
if a * math.sqrt(2) <= d:
    print("Да")
else:
    print("Нет")

# 4.19
s1 = float(input())
s2 = float(input())
r1 = math.sqrt(s1 / math.pi)
a = math.sqrt(4 * s2 / math.sqrt(3))
r2 = a * math.sqrt(3) / 6
r3 = a * math.sqrt(3) / 3
if r1 <= r2:
    print("Круг помещается в треугольнике")
else:
    print("Круг не помещается в треугольнике")
if r3 <= r1:
    print("Треугольник помещается в круге")
else:
    print("Треугольник не помещается в круге")

# 4.20
x1a = float(input())
y1a = float(input())
x2a = float(input())
y2a = float(input())
x1b = float(input())
y1b = float(input())
x2b = float(input())
y2b = float(input())
xmin = min(x1a, x1b)
ymin = min(y1a, y1b)
xmax = max(x2a, x2b)
ymax = max(y2a, y2b)
print(xmin, ymin)
print(xmax, ymax)

# 4.99 а)
a = float(input())
b = float(input())
m = a
if b > m: m = b
print(m)

# 4.99 б)
a = float(input())
b = float(input())
m = a
m = b if b > a else m
print(m)

# 4.100 а)
a = float(input())
b = float(input())
maxn = a
if b > maxn: maxn = b
minn = a
if b < minn: minn = b
print("max =", maxn, "min =", minn)

# 4.100 б)
a = float(input())
b = float(input())
maxn = a if a > b else b
minn = b if a > b else a
print("max =", maxn, "min =", minn)

# 4.101 а)
a = float(input())
b = float(input())
c = float(input())
m = a
if b > m: m = b
if c > m: m = c
print("max =", m)

# 4.101 б)
a = float(input())
b = float(input())
c = float(input())
m = a
if b < m: m = b
if c < m: m = c
print("min =", m)

# 4.102 а)
a = float(input())
b = float(input())
c = float(input())
d = float(input())
m = a
if b > m: m = b
if c > m: m = c
if d > m: m = d
print("max =", m)

# 4.102 б)
a = float(input())
b = float(input())
c = float(input())
d = float(input())
m = a
if b < m: m = b
if c < m: m = c
if d < m: m = d
print("min =", m)

# 4.103
x = float(input())
if x < 0: x = -x
print(x)

# 4.104 а)
a = float(input())
b = float(input())
if a < 0: a = -a
if b < 0: b = -b
print((a + b) / 2)

# 4.104 б)
import math
a = float(input())
b = float(input())
if a < 0: a = -a
if b < 0: b = -b
print(math.sqrt(a * b))

# 4.105
a = float(input())
b = float(input())
if abs(a) > abs(b): a /= 2
print(a)

# 4.106
import math
a = float(input())
b = float(input())
if math.sqrt(b) < a: b *= 5
print(b)

# 4.107
a = int(input())
b = int(input())
c = int(input())
if a % 2 == 0: print(a)
if b % 2 == 0: print(b)
if c % 2 == 0: print(c)

# 4.108
a = float(input())
b = float(input())
c = float(input())
if a >= 0: print(a ** 2)
if b >= 0: print(b ** 2)
if c >= 0: print(c ** 2)

# 4.109
a = float(input())
b = float(input())
c = float(input())
if 1.6 <= a <= 3.8: print(a)
if 1.6 <= b <= 3.8: print(b)
if 1.6 <= c <= 3.8: print(c)

