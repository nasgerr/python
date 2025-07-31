s = input().split()
try:
    if s[0].isdigit() and s[1].isdigit():
        res = int(s[0]) + int(s[1])
    else:
        res = s[0] + s[1]
except:
    print("Error")
finally:
    print(res)