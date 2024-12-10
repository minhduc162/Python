# Tổng căn bậc 2 lồng nhau
import math

x = float(input())
n = int(input())

s = 0 
for _ in range(n):
    s = math.sqrt(x + s) 

S = 1 + s 
print("Giá trị của S = {:.2f}".format(S))
