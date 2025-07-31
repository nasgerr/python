class Test:
    def __init__(self, descr):
        if not 10 <= len(descr) <= 10000:
            raise ValueError()
        self.descr = descr

    def run(self):
        raise NotImplementedError


class TestAnsDigit(Test):
    def __init__(self, descr, ans_digit, max_error_digit=0.01):
        super().__init__(descr)
        if not isinstance(ans_digit, (int, float)) or not isinstance(max_error_digit, (int, float)):
            raise ValueError('недопустимые значения аргументов теста')
        if max_error_digit < 0:
            raise ValueError('недопустимые значения аргументов теста')
        self.ans_digit = ans_digit
        self.max_error_digit = max_error_digit

    def run(self):
        ans = float(input())
        lower = self.ans_digit - self.max_error_digit
        upper = self.ans_digit + self.max_error_digit
        return lower <= ans <= upper


try:
    descr, ans = map(str.strip, input().split('|'))
    ans = float(ans)

    test = TestAnsDigit(descr, ans)

    print(test.run())
except ValueError as e:
    print(e)
except NotImplementedError:
    print("NotImplementedError")