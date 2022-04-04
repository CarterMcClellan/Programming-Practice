Inheritance
  If you have multiple classes which perform the
  same function. Each class should instead inherit
  from a parent class

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
