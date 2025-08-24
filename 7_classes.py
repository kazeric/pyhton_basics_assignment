#Number 1
#  creating the class students 
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


    def display_info(self):
        print(self.name)
        print(self.age)
        print(self.grade)
        print('---')
    

# creating the three student objects
student1 = Student("Eric", 20, "A")
student2 = Student("Bob", 22, "B+")
student3 = Student("John", 19, "A-")

# Call display_info() for each student
student1.display_info()
student2.display_info()
student3.display_info()

print('---')
print('number 1 results')
print('---')


#Number 2

class BankAccount:
    bank_name = "MyBank"

    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    # Add money into the bank account
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive.")

    # Remove money from the bank account
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    #Display account info 
    def display_balance(self):
        print(f"Account Balance: ${self.balance}")

    @classmethod
    def display_bank_name(cls):
        print(f"Bank Name: {cls.bank_name}")


# Create two account objects
account1 = BankAccount("ACC123", 500)
account2 = BankAccount("ACC456", 1000)

# Perform transactions
account1.deposit(200)
account1.withdraw(100)
account1.display_balance()

account2.deposit(500)
account2.withdraw(2000)  # Should show insufficient funds
account2.display_balance()

# Display bank name (class method)
BankAccount.display_bank_name()

print('---')
print('number 2 results')
print('---')


# Number 3
class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__speed = 0

    # Getter and Setter for make
    def get_make(self):
        return self.__make
    
    def set_make(self, make):
        self.__make = make

    # Getter and Setter for model
    def get_model(self):
        return self.__model
    
    def set_model(self, model):
        self.__model = model

    # Getter and Setter for year
    def get_year(self):
        return self.__year
    
    def set_year(self, year):
        self.__year = year

    # Speed control
    def increase_speed(self, value):
        self.__speed += value
        print(f"Speed increased to {self.__speed} km/h")

    def decrease_speed(self, value):
        self.__speed = max(0, self.__speed - value)  # prevent negative speed
        print(f"Speed decreased to {self.__speed} km/h")

    # Display car details
    def display_info(self):
        print(f"Car Details: {self.__year} {self.__make} {self.__model}, Speed: {self.__speed} km/h")



car1 = Car("Toyota", "Corolla", 2020)

# Display initial info
car1.display_info()

# Update attributes using setters
car1.set_make("Honda")
car1.set_model("Civic")
car1.set_year(2022)

# Use speed methods to increase and decrease the speed
car1.increase_speed(50)
car1.decrease_speed(20)

# Display updated info
car1.display_info()

print('---')
print('number 3 results')
print('---')



#Number 4
import math
# original circle class
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius


# Cylinder class (takes Circle object and uses it for the volume)
class Cylinder:
    def __init__(self, circle, height):
        self.circle = circle   # Circle object
        self.height = height

    def volume(self):
        return self.circle.area() * self.height

# testing the circle and cylinder
circle = Circle(5)
print("Circle Area:", circle.area())
print("Circle Circumference:", circle.circumference())

cylinder = Cylinder(circle, 10)   
print("Cylinder Volume:", cylinder.volume())


print('---')
print('number 4 results')
print('---')


#Number 5
# Author class to represent the aggregation relationships in classes
class Author:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

    def display_info(self):
        print(f"Author: {self.name}, Nationality: {self.nationality}")


# Book class (aggregates Author object)
class Book:
    def __init__(self, title, price, author):
        self.title = title
        self.price = price
        self.author = author   # Aggregation: Book "has an" Author

    def display_details(self):
        print(f"Book: {self.title}, Price: {self.price}")
        self.author.display_info()


# Author instance
author1 = Author("Chinua Achebe", "Nigerian")

# Book instances with the first author info
book1 = Book("Things Fall Apart", 1500, author1)
book2 = Book("No Longer at Ease", 1200, author1)

book1.display_details()
book2.display_details()

print('---')
print('number 5 results')
print('---')

#Number 6
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def compare_area(self, other_rectangle):
        if self.area() > other_rectangle.area():
            print(f"Rectangle ({self.length}x{self.width}) has a larger area "
                  f"than Rectangle ({other_rectangle.length}x{other_rectangle.width}).")
        elif self.area() < other_rectangle.area():
            print(f"Rectangle ({self.length}x{self.width}) has a smaller area "
                  f"than Rectangle ({other_rectangle.length}x{other_rectangle.width}).")
        else:
            print(f"Both rectangles have the same area ({self.area()}).")


# Creating the rectangle objects
rect1 = Rectangle(10, 5)
rect2 = Rectangle(7, 8)
rect3 = Rectangle(6, 6)

# Display their areas & perimeters
print("Areas and Perimeters:")
print(f"Rectangle1: Area={rect1.area()}, Perimeter={rect1.perimeter()}")
print(f"Rectangle2: Area={rect2.area()}, Perimeter={rect2.perimeter()}")
print(f"Rectangle3: Area={rect3.area()}, Perimeter={rect3.perimeter()}")

print("Comparisons:")
rect1.compare_area(rect2)
rect2.compare_area(rect3)
rect1.compare_area(rect3)

print('---')
print('number 6 results')
print('---')