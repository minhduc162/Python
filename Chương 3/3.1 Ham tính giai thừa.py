# Tính giai thừa
def giai_thua(n):
    if n < 0:
        return
    elif n == 0 or n == 1:
        return 1
    else:
        gt = 1
        for i in range(2, n + 1):  
            gt *= i
        return gt

try:
    n = int(input("Nhập một số nguyên: "))
    ket_qua = giai_thua(n)
    print(f"Giai thừa của {n} là: {ket_qua}")
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")