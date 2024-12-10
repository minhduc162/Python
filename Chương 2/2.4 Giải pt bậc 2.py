import math 
def ptbac1(a , b) :
    if a == 0 :
        if b == 0 :
            print("VSN")
        else :
            print("VN")
    else :
        print("x = {:.2f}".format(-b/a))
def ptbac2(a, b, c) :
    if a == 0 :
            return ptbac1(b, c)
    else :
        delta = b**2 - 4*a*c 
        if delta < 0 :
            return "VN"
        elif delta == 0 :
            x = -b/(2*a)
            print("x1 = x2 = {:.2f}".format(x))
        else :
            x1 = (-b - math.sqrt(delta)) / (2*a)
            x2 = (-b + math.sqrt(delta)) / (2*a)
            print("x1 = {:.2f}, x2 = {:.2f}".format(x1,x2) )
a, b, c = map(float,input("Nhập hệ số : ").split())
kq = ptbac2(a,b,c)
print (kq)
        


        