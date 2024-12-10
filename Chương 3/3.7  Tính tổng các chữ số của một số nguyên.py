def tong_dem(n):
    s = 0
    dem = 0
    while n != 0:
        s += n % 10
        dem += 1
        n //= 10
    print(f"{dem} {s}")
n = int(input("Nhập số n: "))
if n < 0:
    print("Du lieu sai.")
else:
    tong_dem(n)
