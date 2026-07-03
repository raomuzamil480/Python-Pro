# Multiple Inheritance
# A child class inherits from more than one parent class.
class Father:
    def skills(self):
        print("Father: Driving")

class Mother:
    def talent(self):
        print("Mother: Cooking")

class Child(Father, Mother):
    pass

obj = Child()

obj.skills()
obj.talent()

# Multilevel Inheritance
# A class inherits from a class, and another class inherits from that class.

class Grandfather:
    def house(self):
        print("Grandfather has a house")

class Father(Grandfather):
    def car(self):
        print("Father has a car")

class Son(Father):
    def bike(self):
        print("Son has a bike")

obj = Son()

obj.house()
obj.car()
obj.bike()