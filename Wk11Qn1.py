class Calculator:
    def __init__(self, input1, input2):
        self.input1 = input1
        self.input2 = input2
    def adder(self):
        return self.input1 + self.input2
    def subtractor(self):
        return self.input1 - self.input2
    def multiplier(self):
        return self.input1 * self.input2
    def divider(self):
        return self.input1 / self.input2
    def clear(self):
        self.input1 = 0
        self.input2 = 0

calculator = Calculator(43, 24)
addition = calculator.adder()
print (addition)
subtraction = calculator.subtractor()
print (subtraction)
multiplication = calculator.multiplier()
print (multiplication)
division = calculator.divider()
print (division)
calculator.clear()
print (vars(calculator))
    