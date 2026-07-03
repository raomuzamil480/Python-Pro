class Animal:
    def __init__(self,name,is_live):
        self.name=name
        self.is_live=is_live

    def eat(self):
        print(f"Animal name is {self.name} is eating")

    def sleep(self):
        print(f"Animal name is {self.name} is sleeping  ")

class Dog(Animal):
    def speak(self):
        print(f'bhoo bhoo {self.name}')

class Cat(Animal):
    def speak(self):
        print(f'Meao Meao {self.name}')

d=Dog("Dog",True)
d.eat()
d.sleep()
d.speak()

c=Cat('Cat',True)
c.speak()

