# A base class Person
class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("Name:", self.name)
        print("Age", ":", self.age)


class Education():

    def __init__(self, degree, university, year):
        self.degree = degree
        self.university = university
        self.year = year

    def show(self):
        print("\nEducation qualifications are..... \n")
        print("Qualification:", self.degree, "\nUniversity:", self.university,
              "\nYear:", self.year)


class Account():

    def __init__(self):
        self.balance = 0

    def credit_account(self, amount):
        self.balance += amount

    def check_balance(self):
        print('£' + str(self.balance))

person = Person('Dan Blake', 45)

person.show()

account = Account()

account.credit_account(10000)

account.check_balance()

education = Education('MBA', "London Business School", "2019")
education.show()
