class Calculator:
    def __init__(self, n1, n2):
        print('\n=== __init()__ START ===')
        self.num1 = n1
        self.num2 = n2

    def add(self):
        print('\n=== add() START ===')
        print('num1 + num2 = ', self.num1 + self.num2)

    def subtract(self):
        print('\n=== subtract() START ===')
        print('num1 - num2 = ', self.num1 - self.num2)

cal1 = Calculator(10,20)
cal1.add()
cal1.subtract()