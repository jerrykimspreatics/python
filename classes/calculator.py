
class Calculator:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def add(self):
        return self.n1 + self.n2

    def sub(self):
        return self.n1 - self.n2

    def mul(self):
        return self.n1 * self.n2

    def div(self):
        if self.n2 == 0:
            return "0으로 나눌수 없습니다."
        else:
            return self.n1 / self.n2

cal = Calculator(3, 0);
print(cal.add())
print(cal.sub())
print(cal.mul())
print(cal.div())