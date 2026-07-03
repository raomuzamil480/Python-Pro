# same method but different behaviours
from  abc import ABC ,abstractmethod

class Shap(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shap):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14 * self.radius **2

class Square(Shap):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side **2

saf=[Circle(2),Square(3)]

for s in saf:
    if isinstance(s,Circle):

        print(f" Area of Circle is {s.area()}")
    elif isinstance(s, Square):
        print(f"Area of square is {s.area():.2f}")

