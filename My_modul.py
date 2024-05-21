import math


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("nelze dělit nulou")
        return a / b

    def maximum(self, a, b):
        return max(a, b)

    def minimum(self, a, b):
        return min(a, b)

    def percentage(self, a, b):
        if b == 0:
            raise ValueError("nelze dělit nulou")
        return (a / b) * 100


calc = Calculator()
print(calc.add(2, 3))
print(calc.subtract(7, 2))
print(calc.multiply(3, 4))
print(calc.divide(10, 2))
print(calc.maximum(2, 3))
print(calc.minimum(2, 3))
print(calc.percentage(20, 50))