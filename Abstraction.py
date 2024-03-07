# # Create an abstract class Animal with methods eat() and sleep(), 
# # and derive concrete classes like Dog and Cat from it.

from abc import ABC , abstractmethod
class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass
    @abstractmethod
    def sleep(self):
        pass

class Dog(Animal):
    def eat(self):
        print("Dog is eating")

    def sleep(self):
        print("Dog is sleeping")

class Cat(Animal):
    def eat(self):
        print('Cat is Eating')

    def sleep(self):
        print("Cat is sleeping")

a = Dog()
a.eat()
a.sleep()

b = Cat()
b.eat()
b.sleep()

"""
# # Design a Python class called Shape that serves as an abstract base class for different geometric shapes.
# # Include an abstract method calculate_area() in the Shape class. 
# # Then, create two subclasses Rectangle and Circle inheriting from Shape. 
# # Implement the calculate_area() method in each subclass to calculate the area of a rectangle 
# # and a circle respectively. Finally, demonstrate abstraction by creating objects of both subclasses 
# # and calling the calculate_area() method on each object.


# from abc import ABC , abstractmethod
# class shape(ABC):
#     @abstractmethod
#     def calculate_area(self):
#         pass

# class Rectangle(shape):
#     def __init__(self , lenght , height):
#         self.height = height
#         self.lenght = lenght

#     def calculate_area(self):
#         self.resultOfRectangle =  self.height * self.lenght
#         print("Reactangle: ",self.resultOfRectangle)

# class Circle(shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def calculate_area(self):
#         import math
#         self.resultOfCircle = math.pi * self.radius * self.radius
#         print("Circle: ",self.resultOfCircle)

# a = Rectangle(4,6)
# a.calculate_area()

# b = Circle(7)
# b.calculate_area()
"""

# Design a Python program for a simple bank account management system. 
# Define an abstract base class called Account with abstract methods deposit() and withdraw(). 
# Create subclasses SavingsAccount and CurrentAccount that inherit from Account and 
# implement the deposit() and withdraw() methods based on the account type. 
# Test your program by creating instances of both account types and performing deposit and withdrawal operations.


from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, balance=0):
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

class SavingsAccount(Account):
    def deposit(self, amount):
        self.balance += amount
        print(f"Amount {amount} deposited into Savings Account. Current balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Amount {amount} withdrawn from Savings Account. Current balance: {self.balance}")
        else:
            print("Insufficient funds in Savings Account.")

class CurrentAccount(Account):
    def deposit(self, amount):
        self.balance += amount
        print(f"Amount {amount} deposited into Current Account. Current balance: {self.balance}")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"Amount {amount} withdrawn from Current Account. Current balance: {self.balance}")

savings_account = SavingsAccount(1000)
savings_account.deposit(500)
savings_account.withdraw(200)

current_account = CurrentAccount(2000)
current_account.deposit(1000)
current_account.withdraw(500)
