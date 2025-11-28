#!/usr/bin/python3
"""
Module-6 class BaseGeometry
"""


class BaseGeometry:
    """Class for BaseGeometry"""
    def area(self):
        """function area that raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function that validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Class for Rectangle"""
    def __init__(self, width, height):
        """function for initialization of Rectangle
        with usage of parent class integer_validator"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__height * self.__width

    def __str__(self):
        """Return string representation of the rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """Class for Square that inherits from Rectangle"""
    def __init__(self, size):
        """function for initialization of Square
        with usage of parent class integer_validator"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self._Rectangle__width * self._Rectangle__height

    def __str__(self):
        """Return string representation of the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
