import math
def giaithua(n):
    if n == 0:
        return 1
    else:
        return n * giaithua(n-1)

print("Nhap x va n:")
x, n = map(int, input().split())
print("Nhap ep (0< ep <1):")
ep = float(input())
s = 0
for i in range(n+1):
    if math.fabs(x**i/giaithua(i)) < ep:
        m = i
        break
    else:
        s += x**i/giaithua(i)
print("e^x = {}, gia tri toi han m = {}".format(s, m))