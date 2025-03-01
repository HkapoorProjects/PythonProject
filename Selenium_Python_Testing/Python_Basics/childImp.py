from Selenium_Python_Testing.Python_Basics.classes_demo import Calculator


class ChildImp(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 3, 4)

    def get_full_data(self):
        return self.num + self.num2 + self.summation()


obj = ChildImp()
print(obj.get_full_data())
