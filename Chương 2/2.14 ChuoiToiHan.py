def giaithua(n):
    if n == 0:
        return 1
    else:
        return n * giaithua(n-1)

n = int(input())
s = 0
for i in range(n):
    if 0<1/giaithua(i)<0.01:
        a = i
        break
    else:
        s += 1/(giaithua(2*i+1))
print("S = {}, a = {}".format(s, a))