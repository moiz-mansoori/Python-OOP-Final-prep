
# Create a base class called Shape with a method calculate_area(). 
# Then, create two subclasses Rectangle and Circle inheriting from Shape. 
# Implement the calculate_area() method in each subclass to calculate the area of a rectangle and a circle respectively. 
# Finally, demonstrate polymorphism by creating a list of Shape objects containing instances of both Rectangle and Circle,
# and calling the calculate_area() method on each object in the list.


class shape:
    def calculate():
        pass

class rect(shape):
    def __init__(self , height , lenght):
        self.height = height
        self.lenght = lenght

    def calculate(self):
        return self.height * self.lenght

class circle(shape):
    def __init__(self , radius):
        self.radius = radius

    def calculate(self):
        import math
        return math.pi * self.radius * self.radius
    
a = rect(2,3)
print(a.calculate())

b = circle(4)
print(b.calculate())
