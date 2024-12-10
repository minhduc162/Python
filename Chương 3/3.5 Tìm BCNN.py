
a, b = map(int, input("Nhập hai số a và b: ").split())
if a <= 0 or b <= 0:
    print("Du lieu sai")
else:
    bcnn = max(a, b)
    while True:
        if bcnn % a == 0 and bcnn % b == 0:
            break
        bcnn += 1
    print(bcnn)
