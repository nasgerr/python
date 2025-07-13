class DigitRetrieve:
    def __call__(self, string, *args, **kwargs):
        if string[0] == '-':
            if string[1:].isdigit():
                return int(string)
        elif string.isdigit():
            return int(string)
        return None
