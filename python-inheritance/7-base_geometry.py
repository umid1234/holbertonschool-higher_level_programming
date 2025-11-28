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
