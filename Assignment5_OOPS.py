# Challenge 1: Square Numbers and Return Their Sum
 class Point:

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        sq= (self.x**2)+(self.y**2)+(self.z**2)
        return sq

square= Point(1,2,5)
print(square.sqSum())

# Challenge 2: Implement a Calculator Class

class Calculator:

    def __init__(self, num1,num2):
        self.num1= num1
        self.num2= num2
    def add(self):
        print( self.num1 + self.num2)
    def subtract(self):
        print( self.num1-self.num2)
    def multiply(self):
        print( self.num1 * self.num2)
    def divide(self):
        print( self.num1/self.num2)

obj = Calculator(10, 94)
obj.add()
obj.subtract()
obj.multiply()
obj.divide()

# Challenge 3: Implement the Complete Student Class

class Student:
    def __init__(self):
        self.__name= "Sanju"
        self.__rollNumber= 20

    def setName(self,new_name):
        self.__new_name= new_name
    def getName(self):
        return self.__new_name
    def setRollNumber(self,new_roll):
        self.__new_roll= new_roll
    def getRollNumber(self):
        return self.__new_roll

details= Student()
details.setName("Afridi Islam")
print(details.getName())
details.setRollNumber(10)
print(details.getRollNumber())

# Challenge 4: Implement a Banking Account

class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

account = Account("Ashish", 5000)
print(account.title)
print(account.balance)

savings_account = SavingsAccount("Ashish", 5000, 5)
print(savings_account.title)
print(savings_account.balance)
print(savings_account.interestRate)

# Challenge 5: Handling a Bank Account

class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    def withdrawal(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def getBalance(self):
        return self.balance


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        return (self.balance * self.interestRate) // 100


account1 = SavingsAccount("Ashish", 2000, 5)
account1.deposit(500)
print(account1.getBalance())

account2 = SavingsAccount("Ashish", 2000, 5)
account2.withdrawal(500)
print(account2.getBalance())

account3 = SavingsAccount("Ashish", 2000, 5)
print(account3.interestAmount())
