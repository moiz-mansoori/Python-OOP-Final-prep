
# Create a Python program to calculate the pressure and volume of two different objects:
#  a simple parameter and pipes. Implement the necessary classes and methods to perform these
#  calculations according to the provided information 
# Implement a class named Parameter with the following methods:
# pressure1()
# volume1()
# Create a subclass named Pipes that inherits from the Parameter class.
# Override the pressure1() and volume1() methods to calculate pressure and volume specific to pipes.
# Implement methods pressure2() and volume2() to calculate pressure and volume for pipes using their respective formulas.



class parameter:
    def __init__(self):
        pass
        
    def pressure1(self):
        print("The formula of pressure is f/a")
        self.f_pressure = int(input("Enter the pressure of force: "))
        print("Area =  area = lenght")
        self.a_pressure = int(input("Enter the pressure of area: "))
        print(f"{self.f_pressure} / {self.a_pressure} is {self.f_pressure/self.a_pressure}")
        
    def volume1(self):
        print("   ")
        print("The formula of volume is pi r2")
        self.r_volume = int(input("Enter the volume of radius: ")) 
        print(f"Volume = {3.142* self.r_volume * self.r_volume}")
        
class pipes(parameter):
    def __init__(self):
        super().__init__()
        pass
    def pressure2(self):
        print("   ")
        print("The formula of pressure is f/a")
        self.f_pressure1 = int(input("Enter the pressure of force: "))
        print("Area = lenght * breathe * height")
        print("l = h = w = 3")
        self.a_pressure1 = 3*3*3
        print(f"{self.f_pressure1} / {self.a_pressure1} is {self.f_pressure1 / self.a_pressure1}")
        
    def volume2(self):
        print("   ")
        print("The formula of volume is pi r3")
        self.r_volume1 = int(input("Enter the volume of radius: "))
        print(f"Volume = {3.142* self.r_volume1 * self.r_volume1 * self.r_volume1} ")
        
        
        
        
a = parameter()
a.pressure1()
a.volume1()

b = pipes()
b.pressure2()
b.volume2()





