#Challenge 1:Square Numbers and Return Their sum
class Square:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def sum(self): 
      print(self.x**2+self.y**2+self.z**2)
a=int(input("Enter a x number:"))
b=int(input("Enter a y number:"))
c=int(input("Enter a z number:"))      
obj=Square(a,b,c)
obj.sum() 

#Challenge 2 :Implement a calculator Class
'''class calculator:
    def __init__(self,num1,num2):
      self.num1=num1
      self.num2=num2

    def add(self):
       print(self.num2+self.num1)
    def subtract(self):
       print(self.num2-self.num1)
    def multiply(self):
       print(self.num2*self.num1)
    def divide(self):
       print(self.num2/self.num1)
a=int(input("enter a num1:"))
b=int(input("enter a num2:"))    
obj=calculator(a,b) 
obj.add()
obj.subtract()
obj.multiply()
obj.divide()'''


#Challenge 3:Implement the Complete Student Class
'''class Student:
    def __init__(self):
        self._Studentname=""
        self._Rollnumber=0
     
    def setname(self,name):
        self._Studentname =name 
    def getname(self):
        return self._Studentname   
    def setRollnumber(self,Roll):
        self._Rollnumber=Roll
    def getRollnumber(self):
        return self._Rollnumber
obj=Student()

b=str(input("Enter a Studentname:"))
obj.setname(b)
a=int(input("Enter a Rolnumber:"))
obj.setRollnumber(a)
print("StudentName:",obj._Studentname)
print("RollNumber:",obj._Rollnumber)'''
   

#Challenge 4:Implement a Banking Account
'''class Account:
    def __init__(self,title,Balance):
        self.title=title
        self.Balance=Balance
class SaveingsAccount(Account):
    def __init__(self,title,Balance,interestrate):
        super().__init__(title, Balance)
        self.interestrate = interestrate
        return
t=str(input("Enter a title:"))
b=eval(input("Enter a Balance:"))
I=eval(input("Enter a interestrate:"))
obj=SaveingsAccount(t,b,I)
print((obj.title , obj.Balance,obj.interestrate))
print("Here",obj.title,"is the title and" ,obj.Balance,"is the balance and ",obj.interestrate,"is the interestRate")
'''
# Challenge 5:Handling a Bank Account
'''class Account:
    def __init__(self,title,balance):
        self.title = title
        self.balance = balance
    def withdrawal(self, amount):
      if amount > self.balance:
       print("Insufficient balance")
      else:
        print("Withdrawal:",self.balance-amount)
         
    def deposit(self, amount):
        print("Deposit Result:",self.balance+amount)
    def getBalance(self):
        print("Balance Result:",self.balance)
class SavingsAccount(Account):
    def __init__(self, title, balance, interestRate):
            super().__init__(title, balance)
            self.interestRate = interestRate
    
    def interestAmount(self):
       print("InterestRate Result:",self.balance*self.interestRate//100)

t=str(input("Enter a title:"))
b=int(input("Enter a balance:"))
i=eval(input("Enter a interestRate:"))
obj1=SavingsAccount(t,b,i) 
print("Title:",t)
obj1.getBalance()
a=int(input("Enter a deposit amount:"))
obj1.deposit(a)
print()
obj1.getBalance()
c=int(input("Enter a withdrawal amount:"))
obj1.withdrawal(c)
print()
obj1.getBalance()
print("interestRate:",i)
obj1.interestAmount()'''

