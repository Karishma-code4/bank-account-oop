class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def account_type(self):
        print("bankaccount")

    def deposit(self, amount):
         
         self.__balance += amount
         print("Deposited:", amount)
         print("Balance:", self.__balance)

    def withdraw(self, amount):
        
        if amount <= self.__balance:
            self.__balance -= amount
            print("withdrawn:", amount)
            print("Balance:", self.__balance)
        else:
            print("Insufficient balance")

    def check_balance(self):
        print("Your balance is",self._balance)

    def get_balance(self):
        return self.__balance

    def tranfer(self, amount, other_account):
        if amount <= self.__balance:
             self.__balance -= amount 
             other_account._balance  += amount
        else:
            print("Insufficient balance")

class SavingAccount(BankAccount):
    def add_interest(self):
        balance = self.get_balance()
        interest = balance * 0.05
        self.deposit(interest)



class CurrentAccount(BankAccount):
   
    
    def withdraw(self, amount):
        overdraft_limit = 5000
        if amount > self._balance + overdraft_limit:
           print("Insufficient balance")
        else:
           self._balance -= amount
           print("Withdrawl successful!")

    
 
account = CurrentAccount("Karishma", 2000)
account.withdraw(8000)
account.check_balance()  