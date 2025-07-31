def input_int_numbers():
    s = input().split()
    num = []
    for x in s:
        try:
            n = int(x)
            num.append(n)
        except ValueError:
            raise TypeError
    return tuple(num)

while True:
    try:
        res = input_int_numbers()
        print(" ".join(map(str, res)))
        break
    except TypeError:
        continue