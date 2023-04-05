#!/usr/bin/python3
"""
This module defines a Rectangle class
"""


class Rectangle:
    """
    Defines a Rectangle object
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle object
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Returns the width of the Rectangle object
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the Rectangle object
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Returns the height of the Rectangle object
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the Rectangle object
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Computes the area of the Rectangle object
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Computes the perimeter of the Rectangle object
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the Rectangle object
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = ""
        for i in range(self.__height):
            rect += "#" * self.__width
            if i < self.__height - 1:
                rect += "\n"
        return rect

    def __repr__(self):
        """
        Returns a string representation of the Rectangle object
        that can be used to recreate a new instance
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)
