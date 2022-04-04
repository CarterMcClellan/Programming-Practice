# Abstraction
#    An interface for all other sub-classes to follow

# Note: Interfaces are defined in Python using 
# abstract base class (abc) (both inheritance
# and the @abc decorator are required)

import abc

class Polygon(abc.ABC):
    @abc.abstractmethod
    def area(self, l, w):
        pass

    @abc.abstractproperty
    def n_sides(self):
        pass

class Triangle(Polygon):
    def area(self, l, w):
        return 1/2 * l * w

    def n_sides(self):
        return 3

class Square(Polygon):
    pass

def main():
    triangle = Triangle()
    try:
        square = Square()
    except:
        print("Missing required method 'n_sides' from Square class")

if __name__ == "__main__":
    main()
