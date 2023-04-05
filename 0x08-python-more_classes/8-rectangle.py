#!/usr/bin/python3
"""
Defines a Rectangle class
"""


class Rectangle:
    """
    A class to represent a rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Constructs all the necessary attributes for the Rectangle object
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Retrieves the value of width
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the value of width
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Retrieves the value of height
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the value of height
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Calculates the area of the Rectangle
        """

        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the Rectangle
        """

        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the Rectangle
        """

        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            string = ""
            for i in range(self.__height):
                string += str(self.print_symbol) * self.__width
                if i != self.__height - 1:
                    string += "\n"
            return string

    def __repr__(self):
        """
        Returns a string representation of the Rectangle that can be used to create a new instance of the class
        """

        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Prints a message when an instance of Rectangle is deleted
        """

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle based on the area
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
