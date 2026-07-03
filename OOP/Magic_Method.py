# use __init__,__str__,__eq__ or  many __contain__ for search (like k keyword ha is mein)
# LIKE  print('rao' in b1)
# __add__ for add
# magical method use in python search in google

#build in operator customize behavior

class Book:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"This is {self.name} and {self.age} age"

    def __eq__(self, other):
        return self.name==other.name and self.age==other.age
b=Book('rao',32)
b1=Book('rao',32)
print(b==b1)
print(b)