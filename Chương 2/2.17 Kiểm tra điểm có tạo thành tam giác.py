import math
a, b, c = map(int, input().split())
if a + b <= c or a + c <= b or b + c <= a :
    print("Khong ton tai tam giac.")
else:
    cv = a + b + c
    p = cv / 2
    dt = math.sqrt(p * (p - a) * (p - b) * (p - c))
    if(a == b == c):
        print("Tam giac deu, cv= {}, dt= {:.2f}".format(cv, dt))
    elif (a == b or a == c or b == c) :
        print("Tam giac can, cv= {}, dt= {:.2f}".format(cv, dt))
    else :
        print("Tam giac vuong, cv= {}, dt= {:.2f}".format(cv, dt))