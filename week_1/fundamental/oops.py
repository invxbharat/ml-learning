# oops concept

# class Student:
#     pass


# for private attribute we use __ before the attribute name

class student:

    def __init__(self, name, age, gender):
        self.__name = name # private attribute
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"Name: {self.__name}, Age: {self.age}, Gender: {self.gender}"

    def get_name(self):
        return self.__name


student2 = student("Alice", 22, "Female")

print(student2)
print(student2.get_name())

print(student2._student__name) # Accessing private attribute using name mangling


# inheritance
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def display(self):
        super().display()
        print(f"Employee ID: {self.employee_id}")

class Manager(Employee):
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age, employee_id)
        self.department = department

    def display(self):
        super().display()
        print(f"Department: {self.department}")

person = Person("John", 30)
employee = Employee("Alice", 25, "E123")
manager = Manager("Bob", 35, "M456", "Sales")

person.display()
employee.display()
manager.display()

# can we do multiple inheritance in python? yes we can do multiple inheritance in python

class A:
    def method_a(self):
        print("Method A from class A")
class B:
    def method_a(self):
        print("Method B from class B")
class C(A, B):
    def method_c(self):
        print("Method C from class C")


# how to access the method of class A and B in class C
c = C()

c.method_a()
c.method_a()
c.method_c()

# how to check the type of object in python? we can use isinstance() function to check the type of object in python

print(isinstance(c, C))  # True
print(isinstance(c, A))  # True
print(isinstance(c, B))  # True


# what if both class A and B have same method name? we can use super() function to call the method of parent class in child class
# what happens if both class A and B have same method name? we can use super() function to call the method of parent class in child class
# 

class D(A, B):
    def method_a(self):
        print("Method A from class D")
        super().method_a()  # calling method_a of class A

d = D()
d.method_a()  # Method A from class D
print(C.mro())

A.method_a(c)
B.method_a(c)


# instance method in python is a method that belongs to an instance of a class. It can be called on an instance of the class, and it has access to the instance's attributes and methods. Instance methods are defined using the def keyword, and they take self as their first parameter.
class Demo:
    def show(self):
        print("Instance Method")

demo = Demo()
demo.show()  # calling instance method using instance of class


# Class method in python is a method that belongs to the class rather than an instance of the class. It can be called on the class itself, rather than on an instance of the class. Class methods are defined using the @classmethod decorator, and they take cls as their first parameter.
class Demo:
    company = "ABC"

    @classmethod
    def display(cls):
        print(cls.company)

Demo.display()

# static method in python is a method that belongs to the class rather than an instance of the class. It can be called on the class itself, rather than on an instance of the class. Static methods are defined using the @staticmethod decorator.

class Demo:
    @staticmethod
    def add(a, b):
        return a + b

print(Demo.add(10, 20))