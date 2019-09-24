from abc import ABC

class Expr(ABC):
    pass

class Var(Expr):
    def __init__(self, name = "", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name

class Number(Expr):
    def __init__(self, num=0.0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.num = num
    def print(self):
        print(self.num) # print number attribute

class BinOp(Expr):
    def __init__(self, operator, left, right, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.operator = operator
        self.left = left
        self.right = right

    def eval(self):
        if self.operator == "+":
            return Number(self.left + self.right)
        elif self.operator == "-":
            return Number(self.left - self.right)
        elif self.operator == "*":
            return Number(self.left * self.right)
        elif self.operator == "/":
            return Number(self.left / self.right)
            