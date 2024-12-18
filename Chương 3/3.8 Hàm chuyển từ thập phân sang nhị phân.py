def bin(n) :
    if n == 0 :
        return '0'
    binary = ""
    while n > 0 :
        binary = str(n%2) + binary
        n = n // 2
    return binary

def kq(a, b) :
    for i in range( a,b) :
        print(" {} = {} ".format(i, bin(i)))
        

a, b = map(int, input("Nhập hai số a và b: ").split())
if a < b:
    kq(a, b)
else:
    kq(b, a)
