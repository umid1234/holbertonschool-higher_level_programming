#!/usr/bin/python3
"""
Module-1 rectangle about the usage of getters and setters method acompanied with representation dict work on the classes and their instances
"""
class Rectangle:
    """
    This is how real rectangle in python should be created
    """
    number_of_instances = 0
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        return self.__height
   
    @height.setter
    def height(self, value):
        
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
        
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
    def area(self):
        return self.width * self.height
    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
    def __str__(self):
        if self.height == 0 or self.width == 0:
            return ""
        rect = ""
        for i in range(self.height):
            for _ in range(self.width):
                rect += "#"
            if i != self.height - 1:
               rect += "\n"
        return rect
    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)
    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
