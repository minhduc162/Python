x = float(input("Nhập giá trị x: "))
n = int(input("Nhập giá trị n: "))

if x == 1:
    tong = n + 1
else:
    tong = (1 - x**(n+1)) / (1 - x)

print("Tổng S = {:.2f}".format(tong))  




#nhập 3 số tam giác a,b,c kiểm tra có tồn tại không nếu tính diện tich , chu vi
# nhập tọa độ 3 điểm kiểm tra 3 điểm có tạo thành tam giác không nếu  có tính diện tích chu vi