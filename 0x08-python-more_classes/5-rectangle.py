#!/usr/bin/python3
"""
This module defines a Rectangle class
"""


class Rectangle:
    """
    Defines a rectangle with a width and height
    """
    def __init__(self, width=0, height=0):
        """Initialize the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Get the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Get the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """Return the string representation of the rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            rect = ""
            for i in range(self.height):
                rect += "#" * self.width
                if i < self.height - 1:
                    rect += "\n"
            return rect

    def __repr__(self):
        """Return the representation of the rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Print the message when the rectangle is deleted"""
        print("Bye rectangle...")