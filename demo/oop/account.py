class SavingsAccount:
    def __init__(self, acno, ahname, balance=0):
        # Object Attributes
        self.acno = acno
        self.ahname = ahname
        self.__balance = balance

    def show(self):
        print(self.acno)
        print(self.ahname)
        print(self.__balance)

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance += amount
        else:
            raise ValueError("Insufficient Balance")

    def getBalance(self):
        return self.__balance


a1 = SavingsAccount(1, "Steve", 10000)
print(a1.__dict__)
print("Balance", a1.getBalance())
