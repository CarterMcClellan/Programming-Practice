
# Abstraction
An interface for all other sub-classes to follow

Note: Interfaces are defined in Python using 
abstract base class (abc) (both inheritance
and the @abc decorator are required)
```python
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
```

# Encapsulation
The principle of only modifying members of a class
from a single function.

Note: Private variables are denoted within Python
with the usage of "__"

```python
class Car:
    def __init__(self):
        self.color = "Red"

        # private variable
        self.__brand = "BMW"

    def get_brand(self):
        return self.__brand


def main():
    my_car = Car()
    print(my_car.color)

    try:
        print(my_car.__brand)
    except:
        print(
            "Cannot access private members of a class through usage of the '.' operator"
        )

    print(my_car.get_brand())


if __name__ == "__main__":
    main()



class Car:
    def __init__(self):
        self.color = "Red"

        # private variable
        self.__brand = "BMW"

    def get_brand(self):
        return self.__brand


def main():
    my_car = Car()
    print(my_car.color)

    try:
        print(my_car.__brand)
    except:
        print(
            "Cannot access private members of a class through usage of the '.' operator"
        )

    print(my_car.get_brand())


if __name__ == "__main__":
    main()
```


# Inheritance
  If you have multiple classes which perform the
  same function. Each class should instead inherit
  from a parent class

```python
class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self):
        return f"First Name: {self.first_name} Last Name: {self.last_name}"

class Student(Person):

    def __init__(self, first_name, last_name, university):
        super().__init__(first_name, last_name)
        self.university = university

    def get_university(self):
        return f"University: {self.university}"

def main():
    student1 = Student("Carter", "McClellan", "University of Wisconsin - Madison")
    print(student1.get_name())
    print(student1.get_university())

if __name__ == "__main__":
    main()
```

# Polymorphism 
When 2 different classes share the same function name

Note: When talking about polymorphism is not guaranteed, 
that they inherit from the same class, or that they 
follow the same interface.

```python
class Knight:
    def move(self):
        return "Knights move in an L" 

class Bishop
    def move(self):
        return "Bishops move along a diagonal"
```