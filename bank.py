# A base class Person
class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("Name:", self.name)
        print("Age", ":", self.age)


class Account():

    def __init__(self):
        self.balance = 0

    def credit_account(self, amount):
        self.balance += amount

    def check_balance(self):
        print('£' + str(self.balance))




person = Person('Dan Blake', 45)

person.show()

account = Account();

account.credit_account(10000)

account.check_balance()
