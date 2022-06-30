'''
Banking System Using OOP

Parent Class : User
Holds details about an user
has a function to show user details

Child Class : Bank 
Stores details about account balance
Stores details about the amount 
Allows for deposits, withdrawal, view_balance

#Parent Class: User 
#Has a function to show user details
#Child Class : Bank
#Stores details about the account balance
#Stores details about the amount
#Allows for deposits, withdraw, view_balance
'''

class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Personal Details")
        print("")
        print("Name ", self.name)
        print("Age ", self.age)
        print("Gender ", self.gender)

#Attribute = variables
#function  = method = behavior
ali = User("Johaz", 21,"Males")
print(ali.show_details())

# CHild class bank
class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance = 0

    def deposit(self, amount) :
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Account balance has been updated : RM", self.balance)

    def withdraw(self, amount) :
        self.amount = amount
        if(self.amount > self.balance) :
            print("Insufficient Funds | Balance Available : RM", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account balance has been updated : RM", self.balance)
    
    def view_balance(self) : 
        self.show_details()
        print("Account balance has been updated : RM", self.balance)

johan = Bank('johan', 20, 'male')
johan.deposit(1000)
johan.withdraw(900)
johan.show_details()
johan.view_balance()






