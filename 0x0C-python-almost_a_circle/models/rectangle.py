#!/usr/bin/python3
"""class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """
        class Rectangle implements Base.
        Methods:
           __init__()
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
           Initialize a new Rectangle.

           Args:
               width (int): The width of the Rectangle.
               height (int): The height of the Rectangle.
               x (int): The x coordinate of the Rectangle.
               y (int): The y coordinate of the Rectangle.
               id (int): The identity of the Rectangle.
           Raises:
               TypeError: If either width or height is not an int
               ValueError: If either width or height <= 0.
               TypeError: If either x or y is not an int
               ValueError: If either x or y < 0.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ getter function for __width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter function for width """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """ getter function for __height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter function for height """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """ getter function for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter function for x """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """ getter function for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter function for width """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """ returns the area of the Rectangle """
        return (self.width * self.height)

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        rectangle = self.y * "\n"
        for i in range(self.height):
            rectangle += (" " * self.x)
            rectangle += ("#" * self.width) + "\n"

        print(rectangle, end='')

    def __str__(self):
        """returns the print() and str() representation of the Rectangle"""
        return "[Rectangle] ({} {}/{} - {}/{}".format(self.id,
                                                      self.x, self.y,
                                                      self.width, self.height)

    def update(self, *args, **kwargs):
        """
            assigns key/value argument to attributes
            kwargs is skipped if args is not empty
            Args:
                *args - variable number of no-keyword args
                **kwargs - variable number of keyworded args
        """
        if args != None and len(args) != 0:
            list_atr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {'x': getattr(self, "x"), 'y': getattr(self, "y"),
                'id': getattr(self, "id"), 'height': getattr(self, "height"),
                'width': getattr(self, "width")}
