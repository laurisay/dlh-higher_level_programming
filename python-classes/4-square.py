@size.setter
def size(self, value):
    """Set the size of square"""

    if type(value) is not int:
        raise TypeError("size must be an integer")

    if value < 0:
        raise ValueError("size must be >= 0")

    self.__size = value
