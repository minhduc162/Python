def giaithua(n):
    if n == 0:
        return 1
    else:
        return n *giaithua(n-1)

n = int(input())
s = 0
for i in range(n):
    s += 1/(giaithua(2*i+1))
print("S = {}".format(s))

m = 1 
kq = 0
while kq < 1000:
    kq += m
    m += 1
print("m = {}".format(m-1))