#!/usr/bin/env python3
"""
Module 9-student
Defines a class Student
"""


class Student:
    """Class that defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return the dictionary representation of a Student"""
        return self.__dict__
