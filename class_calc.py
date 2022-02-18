class Calculator:
    def __init__(self, number1, number2):
        self.num1 = number1
        self.num2 = number2
        
    def add(self):
        return self.num1 + self.num2
    
    def sub(self):
        return self.num1 - self.num2
    
    def mul(self):
        return self.num1 * self.num2
    
    def div(self):
        return self.num1 / self.num2
    
    def decision(self, user_decision):
        if user_decision == '+':
            return self.add()
        elif user_decision == '-':
            return self.sub()
        elif user_decision == '*':
            return self.mul()
        elif user_decision == '/':
            return self.div()
