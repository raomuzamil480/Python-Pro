# @property
# use to add additional benifits when read write and delete attributs

# geetr setter and deleter method

class Angle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    # string method
    def __str__(self):
        return f"Width = {self._width}, Height = {self._height}"

    # Getter
    @property
    def width(self):
        return self._width

    # Setter
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be > 0")

    # Deleter
    @width.deleter
    def width(self):
        print("Width deleted")
        del self._width

a = Angle(10, 5)

# Getter
print(a.width)

#setter
a.width = 20
print(a.width)

#deleter
del a.width