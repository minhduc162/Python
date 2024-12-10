
a, b = map(float,input().split())
if a == 0 :
    if b <= 0 :
        print("VN")
    else :
          print("VSN")
else :
    if a > 0 :
        print("x > {:.2f}".format(-b/a))
    else :
        print("x < {:.2f}".format(-b/a))