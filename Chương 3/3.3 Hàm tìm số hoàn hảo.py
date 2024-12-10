def hoan_hao(n):
    s = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            s += i
    return s == n

def kq(a, b):
    dem = 0
    for i in range(a, b + 1):
        if i > 0 and hoan_hao(i):
            print(i, end=" ")
            dem += 1
    if dem == 0:
        print("Khong co")


a, b = map(int, input("Nhập hai số a và b: ").split())
if a <= b:
    kq(a, b)
else:
    kq(b, a)
