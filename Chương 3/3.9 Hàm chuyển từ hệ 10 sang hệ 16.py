def swap(c):
    if '0' <= c <= '9':
        return ord(c) - 48
    if 'A' <= c <= 'F':
        return {
            'A': 10,
            'B': 11,
            'C': 12,
            'D': 13,
            'E': 14,
            'F': 15
        }[c]
    if 'a' <= c <= 'f':
        return {
            'a': 10,
            'b': 11,
            'c': 12,
            'd': 13,
            'e': 14,
            'f': 15
        }[c]
    return -1

def check(s):
    for i in range(len(s) - 1, 1, -1):
        if swap(s[i]) == -1:
            return False
    return True


s = input("Nhập chuỗi: ")
if s[:2] == "0x":
    if not check(s):
        print("Invalid input")
    else:
        n = 0
        x = 1
        for i in range(len(s) - 1, 1, -1):
            n += swap(s[i]) * x
            x *= 16
        print(n)
else:
    print("Invalid input")
