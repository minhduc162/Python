def giaithua(n):
    if n == 0:
        return 1
    else:
        return n * giaithua(n-1)

n = int(input())
s = 0
l = 0
for i in range(1,n+1):
    s += giaithua(i)
for i in range(1,n+1,2):
    l += giaithua(i)
print("S = {}, S(le) = {}".format(s, l))