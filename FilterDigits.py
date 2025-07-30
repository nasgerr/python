def is_integer(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

lst_in = input().split()
integers = filter(is_integer, lst_in)
res = sum(map(int, integers))
print(res)