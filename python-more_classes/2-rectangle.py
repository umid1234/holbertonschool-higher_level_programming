#!/usr/bin/python3
"""
Module-1 rectangle about the usage of getters and setters method acompanied with representation dict work on the classes and their instances
"""
class Rectangle:
    """
    This is how real rectangle in python should be created
    """
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
    def area(self):
        return self.width * self.height
    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
