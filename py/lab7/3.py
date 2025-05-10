class bank:
    def __init__(self):
        self.details={}
    def createaccount(self,accno,balance=0):
        self.details[accno]=balance
    def deposit(self,accno,amount):
        if accno in self.detais:
            self.details[accno]+=amount
    def withdraw(self,accno,amount):
        if accno in self.details and amount<=self.details[accno]:
            self.details[accno]-=amount
    def display(self,accno):
        if accno in self.details:
            print(accno,":",self.details[accno])
a=bank()
while 1:
 c=int(input('''enter 1 for create account
enter 2 for deposit
enter 3 for withdraw
enter 4 for display
enter 5 to exit:'''))
 match c:
     case 1:
         b=int(input('enter the value to account no:'))
         c=int(input('enter the initial amount:'))
         a.createaccount(b,c)
     case 2:
         b=int(input('enter the value to account no:'))
         c=int(input('enter the amount:'))
         a.deposit(b,c)
     case 3:
         b=int(input('enter the value to account no:'))
         c=int(input('enter the amount:'))
         a.withdraw(b,c)
     case 4:
         b=int(input('enter the value to account no:'))
         a.display(b)
     case 5:
         break
