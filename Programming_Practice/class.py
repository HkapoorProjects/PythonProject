class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name, "Your average score is:", sum / 3)


s1 = Student("Harshil", [98, 97, 96])
s1.get_avg()
