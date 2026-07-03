# super metHod or function call in child class method from a parent class (superclass)

class Person:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def intro(self):
        print(f"My name is {self.name},from natural {self.color}")

class Man(Person):
    def __init__(self,name,color,age):
        super().__init__(name,color)
        self.age=age
    def intro(self):
        super().intro()
        print(f"My age is {self.age} ")

M=Man('Rao',"brown",21)
M.intro()