def ucln(a, b):
    while a != b:
        if a < b:
            b -= a
        else:
            a -= b
    return a


x, y, z = map(int, input("Nhập ba số x, y, z: ").split())
if x > 0 and y > 0 and z > 0:
    print(ucln(x, ucln(y, z)))
else:
    print("DL sai.")
