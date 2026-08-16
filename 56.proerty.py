# @property = Decorator used to define a method as a property (it can be accessed like an attribute)
#             Benefit: add addtional logic when read, write , or delete attributes
#             Gives you getter, setter, and deleter method

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return f"{self._width:.1f}cm"
    
    @property
    def height(self):
        return f"{self._height:.1f}cm"
    
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greader than zero!")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greader than zero!")

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted!")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted!")
    
rectangle = Rectangle(3, 5)

rectangle.width = 0
rectangle.height  = 10
del rectangle.width
del rectangle.height

print(rectangle.width)
print(rectangle.height)