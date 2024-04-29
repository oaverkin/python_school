class Calc:
    def add(self, a, b):
        result = a + b
        print(f"{a} + {b} = {result}")

    def subtract(self, a, b):
        result = a - b
        print(f"{a} - {b} = {result}")

    def multiply(self, a, b):
        result = a * b
        print(f"{a} * {b} = {result}")

    def divide(self, a, b):
        if b == 0:
            return print(f"{a} / {b} -> Error: Cannot divide by zero")
        result = a / b
        print(f"{a} / {b} = {round(result, 1)}")


calc = Calc()
calc.add(5, 6)
calc.subtract(4, 3)
calc.multiply(2, 3)
calc.divide(5, 2)
calc.divide(5, 0)

# 5 + 6 = 11
# 4 - 3 = 1
# 2 * 3 = 6
# 5 / 2 = 2.5
# 5 / 0 -> Error: Cannot divide by zero

