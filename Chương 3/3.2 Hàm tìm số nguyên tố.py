#tìm số nguyên tố 
def ktr(num) :
    if num <= 1 :
        return False
    for i in range (2, int(num**0.5) +1):
        if num % i == 0:
            return False 
    return True
def timsonguyento(n):
    snt = []
    for i in range(2, n + 1):
        if ktr(i):
            snt.append(i)
    return snt 

n = int(input("Nhập số n: "))
kq = timsonguyento(n)
print(f"Các số nguyên tố trong khoảng (1, {n}): {kq}")

