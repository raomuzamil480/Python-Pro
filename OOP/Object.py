# Object is a bundle of related atibutes   variable and method(funtion)

# class is blue print used to design the structure and layout of the object

class Car:
    def __init__(self,model,age):
        self.model=model
        self.age=age
    def Run(self):
        print(f"The Car is {self.model}")

c1=Car('BMW',21)
c1.Run()

