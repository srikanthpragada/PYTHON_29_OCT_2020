class InsufficientBalanceError(Exception):
    def __init__(self, balance):
        self.balance = balance

    def __str__(self):
        return f"Insufficient Balance. Available balance is {self.balance}"


class SavingsAccount:
    # Static variable or Class attribute
    minbal = 5000

    @staticmethod
    def setMinbal(minbal):
        SavingsAccount.minbal = minbal

    @staticmethod
    def getMinbal():
        return SavingsAccount.minbal

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
        if self.__balance - SavingsAccount.minbal >= amount:
            self.__balance += amount
        else:
            raise InsufficientBalanceError(self.__balance)

    def getBalance(self):
        return self.__balance


# SavingsAccount.setMinbal(10000)
# print(SavingsAccount.minbal)
a1 = SavingsAccount(1, "Steve", 10000)
try:
    a1.withdraw(20000)
except InsufficientBalanceError as ex:
    print(ex)
    print(ex.balance)


# print(a1.__dict__)
# print("Balance", a1.getBalance())
