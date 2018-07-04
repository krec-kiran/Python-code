class Account(object):

    def __init__(self, holder, number, balance, credit_line=1500):
        self.__Holder = holder
        self.__Number = number
        self.__Balance = balance
        self.__CreditLine = credit_line
        self._City = "London"

    def deposit(self, amount):
        self.__Balance = amount

    def withdraw(self, amount):
        if(self.__Balance - amount < -self.__CreditLine):
            # coverage insufficient
            return False
        else:
            self.__Balance -= amount
            return True

    def balance(self):
        return self.__Balance

    def transfer(self, target, amount):
        if(self.__Balance - amount < -self.__CreditLine):
            return False
        else:
            self.__Balance -= amount
            target.__Balance += amount
            return True


account = Account("Kiran", 567, 80000)
print(account._City)
print(account.balance())
