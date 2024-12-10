import math 
c1, c2, c3 = map(int,input().split())
if c1 > 0 and c2 >0 and c3 > 0 :
    if c1 + c2 > c3 or c1 + c3 > c2 or c2 + c3 > c1 :
        chuvi = c1 + c2 + c3
        p = chuvi / 2
        dientich = math.sqrt(p * (p - c1) * (p - c2) * (p - c3))
        print("Chu vì tam giác là : {:.2f}, Diện tích tam giác là : {:.2f}".format(chuvi, dientich))
    else : 
        print("Đây không phải là tam giác")
else : 
    print("Giá trị phải dương")