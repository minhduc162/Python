a, b, c = map(int, input().split())
if a == 0:
    if (b == 0):
        if (c == 0):
            print("VSN.")
        else:
            print("VN.")
    else:  
        kq =float(-c/b)
        print("x= {:.2f}".format(kq))
else:
    delta = float(b**2 - 4*a*c)
    if delta <0:
        print("VN.")
    elif delta == 0:
        kq = -b/2*a
        print("x1= x2= {:.2f}.".format(kq))
    else:
        x1 = (-b + delta**0.5)/2*a
        x2 = (-b - delta**0.5)/2*a
        print("x1= {:.2f}, x2= {:.2f}.".format(x1, x2))