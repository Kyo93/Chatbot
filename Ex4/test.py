class MyClass:
    x = 5
    y = 6


p1 = MyClass()
print(p1.y)


class Persion:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def printname(self):
        print("Hello my name is "+ self.name)
p1=Persion("Thiep",27)
#p1.printname()
print(p1.name, p1.age)


