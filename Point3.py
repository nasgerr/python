class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

s = input().split()
try:
    if s[0].isdigit() and s[1].isdigit():
        pt = Point(int(s[0]), int(s[1]))
    else:
        pt = Point()
except:
    print("Error")
finally:
    print(f"Point: x = {pt._x}, y = {pt._y}")


