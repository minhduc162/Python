def bin(n):
    binary = []
    while n != 0:
        binary.append(n % 2)
        n //= 2
    for bit in reversed(binary):
        print(bit, end=" ")

def kq(a, b):
    for i in range(a, b + 1):
        print(f"{i}: ", end="")
        bin(i)
        print() 

a, b = map(int, input("Nhập hai số a và b: ").split())
if a < b:
    kq(a, b)
else:
    kq(b, a)
