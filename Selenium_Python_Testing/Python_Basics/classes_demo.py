# Notes:
# 1. Self keyword is mandatory for calling variable names into methods
# 2. Instance and class variables have whole different purpose
# 3. Constructor name should be __init__
# 4. New keyword is not required when creating object like other programming language
class Calculator:
    num = 100

    def __init__(self, a, b):
        self.first_number = a
        self.second_number = b
        print("I am getting call whenever object is created")

    def get_data(self):
        print("I am now executing as a method in the class ")

    def summation(self):
        return self.first_number + self.second_number


obj = Calculator(5, 6)
obj.get_data()
print(obj.num)

obj1 = Calculator(2, 3)
obj1.get_data()
print(obj1.summation())
