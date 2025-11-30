#!/usr/bin/env python3
"""
Module 10-student
Defines a class Student
"""


class Student:
    """Class that defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student"""
        self.first_name = first_name
        self.last.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return dictionary representation of Student.
        If attrs is a list of strings, return only those attributes.
        Otherwise return all attributes.
        """
        if (isinstance(attrs, list) and
                all(isinstance(item, str) for item in attrs)):
            return {key: getattr(self, key)
                    for key in attrs if hasattr(self, key)}
        return self.__dict__
