def hex_to_dec(hex_str) :
    if not hex_str.startswith("0x") or any(c not in "0123456789abcdefABCDEF" for c in hex_str[2:]) :
        return "Giá trị không phải là số thập lụclục phân"
    try:
        return int(hex_str, 16)
    except:
        return"Giá tri không hợp lệ"
a = input("Nhập chuỗi: ")
result = hex_to_dec(a)
if result == "Giá trị không phải là số thập phân":
    print(result)
else :
    print("{} --> {}".format(a,result))



def dec_to_hex(n) :
    if n < 0:
        return "Giá trị không hợp lệ"
    char = "0123456789ABCDEFabcdef"
    hex_str = ""
    while n > 0 :
        hex_str = char[n % 16] + hex_to_dec
        n //= 16
    return hex_str if hex_str else "0"
try :
    n = int(input("Nhập số nguyên: "))
    print(dec_to_hex(n))
except :
    print("Giá trị không hợp lệ")
