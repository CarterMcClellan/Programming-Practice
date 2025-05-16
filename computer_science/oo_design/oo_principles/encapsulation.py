Encapsulation
   The principle of only modifying members of a class
   from a single function.

Note: Private variables are denoted within Python
with the usage of "__"


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
