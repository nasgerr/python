lst_in = input().split()
def is_digit(x):
    try:
        return int(x)
    except:
        try:
            return float(x)
        except:
            return x

lst_out = list(map(is_digit, lst_in))