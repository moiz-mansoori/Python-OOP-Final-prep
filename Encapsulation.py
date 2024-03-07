# Public Encapsulation

class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num1 - self.num2

a = int(input("Enter first digit: "))
b = int(input("Enter 2nd digit: "))

a1 = Calculator(a,b)
print(a1.add())
print(a1.subtract())

# Private Encapsulation

class Match:
    def __init__(self, team1 , team2):
        self.team1 = team1
        self.__team2 = team2
        
    def __teams(self):
        print(f"Match between {self.team1} vs {self.__team2} on Wednesday")
        
    def again(self):
        self.__teams()
        
a = Match("Pakistan" , "NewZealand")
a.again()

# Protected Encapsulation

class Vehicle:
    def __init__(self, speed=0):
        self._speed = speed

    def _accelerate(self, amount):
        self._speed += amount
        print(f"Vehicle accelerated by {amount} units. Current speed: {self._speed}")

class Car(Vehicle):
    def accelerate(self, amount):
        self._accelerate(amount)

car = Car()
car.accelerate(60)




# BankAccount class with encapsulated attributes

class BankAccount:
    def __init__(self, name, account_type, balance=0.0):
        self._balance = balance  
        self.name = name  
        self._account_type = account_type 

    def get_balance(self):  
        return self._balance

    def _set_balance(self, new_balance):  
        if new_balance >= 0:
            self._balance = new_balance
        else:
            raise ValueError("Balance cannot be negative")

    def deposit(self, amount):
        self._set_balance(self._balance + amount)

    def withdraw(self, amount): 
        if amount <= self._balance:
            self._set_balance(self._balance - amount)
        else:
            raise ValueError("Insufficient funds")

    def get_account_type(self): 
        return self._account_type


account = BankAccount("John Doe", "Savings", 1000.0)

print(f"Account holder: {account.name}") 
print(f"Balance: ${account.get_balance()}") 
print(f"Account type: {account.get_account_type()}") 

account.deposit(500.0)
print(f"Balance after deposit: ${account.get_balance()}")

account.withdraw(200.0)
print(f"Balance after withdrawal: ${account.get_balance()}")
