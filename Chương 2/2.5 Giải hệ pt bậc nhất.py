  
a, b , c = map(float, input("Nhập hệ số của phương trình thứ nhất").split())
d, e , f = map(float, input("Nhập hệ số của phương trình thứ nhất").split())
D = a * e - b * d
Dx = c * e - b * f
Dy = a * f - c * d
if D == 0 : 
    if Dx == 0 and Dy == 0:
        print("VSN")
    else :
        print("VN")
else :
    x = Dx / D
    y = Dy / D
    print("x = {:.2f}; y = {:.2f}".format(x,y))


