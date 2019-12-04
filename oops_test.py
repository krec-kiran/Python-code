

class Restuarant():
    """
    This class implements Restuarant base class.

    Parameters
    ----------
    restuarant_name : string
    cuisine_type : string

    Attributes
    ----------
    number_served : integer
        number of customers served on a given day

    """

    def __init__(self, restuarant_name, cuisine_type):
        self.restuarant_name = restuarant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restuarant(self):
        print(self.restuarant_name, self.cuisine_type, self.number_served)

    def open_restuarant(self):
        print(self.restuarant_name + ' is open today')

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, today_numbers):
        self.number_served += today_numbers


class IceCreamStand(Restuarant):
    def __init__(self, name, type):
        super().__init__(name, type)
        self.flavours = ['Vanilla', 'Strawberry']

    def describe_restuarant(self):
        print(self.restuarant_name, self.cuisine_type, self.flavours)


icecreamvan = IceCreamStand('Joy', 'icecream shop')
icecreamvan.describe_restuarant()

sagar_restuarant = Restuarant('Sagar', 'South Indian')
benares_restuarant = Restuarant('Benares', 'North Indian')
mayfair_restuarants = [sagar_restuarant, benares_restuarant]

for restuarant in mayfair_restuarants:
    print(restuarant.describe_restuarant())


sagar_restuarant.open_restuarant()
benares_restuarant.open_restuarant()

sagar_restuarant.describe_restuarant()
benares_restuarant.describe_restuarant()

sagar_restuarant.describe_restuarant()
sagar_restuarant.set_number_served(10)
sagar_restuarant.describe_restuarant()

sagar_restuarant.increment_number_served(25)
sagar_restuarant.describe_restuarant()


from random import randint


class Dice():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self):
        print(randint(1, self.sides))


sided_dice_6 = Dice()
for count in range(5):
    sided_dice_6.roll_dice()

sided_dice_10 = Dice(10)
for count in range(5):
    sided_dice_10.roll_dice()

sided_dice_20 = Dice(20)
for count in range(5):
    sided_dice_20.roll_dice()


print('give me two numbers and I will divide them')
print('type q to quit')

while True:
    first = input('First number')
    if first == 'q':
        exit(0)
    second = input('Second number')
    try:
        ans = int(first) / int(second)
    except Exception as e:
        print(type(e))
    else:
        print(ans)


class Ticket:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price < 0:
            print('Nice try!')
        else:
            self._price = new_price


t = Ticket(42)
t.price = -24
print(t.price)


class Student:
    def __init__(self):
        self.name = 'Kiran'
        self._roll_no = '123'
        self.__address = '7 Primrose Walk'


x = Student()
x._roll_no = int(x._roll_no) + 145

print(x._roll_no)

name = '167'

stud = Student()

stud._roll_no = '178'
print(stud._roll_no)


class HomeStudent(Student):
    def __init__(self):
        super().__init__()
        self._roll_no = '145'


home_stud = HomeStudent()

home_stud._roll_no = '190'

print(home_stud._roll_no)

student = Student()
student.name = 'Mike'
print(student.name)

home_student = Student()
home_student._roll_no = '155'
print(home_student._roll_no)


print(student.__address)


class A():

    def __init__(self):
        self.__priv = "I am private"
        self._prot = "I am protected"
        self.pub = "I am public"


x = A()
print(x.pub)
x.pub = x.pub + 'I can be chaged outside'
print(x.pub)

print(x._prot)
x._prot = x._prot + 'I can be chaged outside'
print(x._prot)

print(x.__priv)
x.__priv = x.__priv + 'I can be chaged outside'
print(x.__priv)

cities = ["Berlin", "Vienna", "Zurich"]
iter_obj = iter(cities)
print(iter_obj)
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))

iterators are one, in which __next__ is defined and called when next() is called
    list is iterable likewise, tuple, dictionary and other data structures


def salutation(fn):
    def new(*args):
        return 'Mr ' + str(fn(*args))
    return new


@salutation
def get_name(name):
    return name


print(get_name('Kiran'))


def convert_to_pounds(fn):
    def new(*args):
        return '£' + str(fn(*args) * 2)
    return new


@convert_to_pounds
def price(amount, tax_rate):
    dollars = amount + amount * tax_rate
    print('$' + str(dollars))
    return dollars


print(price(100, 0.1))

Yield - generators


def cubic_generator(val):
    for i in range(val):
        yield i**3


for i in cubic_generator(5):
    print(i, end=':')

cube_gen = cubic_generator(7)

print(next(cube_gen))
print(next(cube_gen))
print(next(cube_gen))
print(next(cube_gen))
print(next(cube_gen))
print(next(cube_gen))
print(next(cube_gen))

keys = ['a', 'b', 'c']
vals = [3, 2, 1]

print(list(zip(keys, vals)))
d = {k: v for k, v in zip(keys, vals)}
print(d)


print(list(map(hash, ['1', '2', '3', '4'])))
print(hash('2'))

import hashlib - md5 - sha
text = 'a'
k = hashlib.md5('a'.encode())
print(k.digest())

serialize and deserialize

import pickle
with open('book.pickle', 'wb') as f:
    pickle.dump(data, f)

with open('book.pickle', 'rb') as f:
    pickle.load(data, f)

import json

with open('book.pickle', 'w', indent=3) as f:
    json.dump(data, f)

with open('book.pickle', 'r') as f:
    json.load(data, f)

A = [21, 12, -3, 42, 15, 61, 117, -80, 19]

print(A[::-1])
print(A[3:] + A[:3])
print(A[:-2])
print(A[-2:])

print(A.reverse())
print(A)
print(A.sort())
print(A)


from collections import defaultdict

food_list = 'spam spam milk spam eggs spam eggs'.split()
food_count = defaultdict(lambda: 2)
for food in food_list:
    food_count[food] += 1

print(food_count)

ice_cream = defauldict(lambda: 'Vanilla')

ice_cream['Sarah'] = 'Chunky Monkey'
ice_cream['Abdul'] = 'Butter Pecan'
print(ice_cream['Sarah'])
print(ice_cream['Kiran'])

import array

arr = array.array('c', (1, 2, 3))

print(arr)

print(list('123'))

from collections import namedtuple

Person = namedtuple('Person', 'name,age,sex')

citizen = Person('Kiran', 43, 'M')

print(citizen)
print(citizen.name)
print(citizen.age)
print(citizen.sex)

from struct import Struct

MyStruct = Struct('i?f')

data = MyStruct.pack(12, False, 43.289)

print(data)

print(MyStruct.unpack(data))


from collections import namedtuple

House = namedtuple('House', 'number,address,city,postcode')

my_house = House(7, 'Primrose Walk', 'Paddock Wood', 'TN126BJ')

print(my_house)
print(my_house.address)
print(my_house.postcode)

my_house.postcode = 'BN212YP'

print(my_house.postcode)

from typing import NamedTuple  # >= Python.3.6.0


class Employee(NamedTuple):
    name: str
    department: str
    salary: int
    is_remote: bool = False  # >= Python.3.6.1


bob = Employee(name='Bob', department='IT', salary=10000, is_remote=True)

print(bob)

from types import SimpleNamespace

car = SimpleNamespace(color='Red', mileage=12367, auto=False)

my_car = dict(color='Red', mileage=12367, auto=False)

print(car)
print(car.color)

print(my_car)
print(my_car['color'])

Dict / Tuples / NamedTuple / typing.NamedTuple / types.SimpleNamespace(attribute access) / Structs


from collections import namedtuple
Person = namedtuple('Person', 'name,age,sex,postcode')

employee = Person('Kiran', 45, 'M', 'TN126BJ')
print(employee)
print(employee.name)
print(employee.postcode)

s = ('Arya', 12, 'TN126BJ')
print(s[0])

from collections import Counter

inventory = Counter()

loot = {'bread': 2, 'sword': 1}

inventory.update(loot)

print(inventory)

more_loot = {'bread': 5, 'apple': 15}

inventory.update(more_loot)

print(inventory)

print(len(inventory))
print(sum(inventory.values()))

for k in inventory.keys():
    print(k)

letters = {'a': 2, 'b': 7, 'c': 10}
print(letters)
for k in letters.keys():
    print(k)
for k in letters.values():
    print(k)

letters['c'] += 10
print(letters)

letters['k'] = 25
print(letters)
del letters['k']
print(letters)

vowels = set()
print(vowels)

vowels = {'a', 'e', 'i', 'o', 'u'}

print(vowels)

vowels.update('k')

print(vowels)

from collections import deque

d = deque()
d.append('cat')
d.append('mouse')
d.append('dog')
print(d)

print(d.pop())
print(d.pop())
print(d.pop())

d.appendleft('tiger')

print(d.popleft())
print(d.popleft())
print(d.popleft())
print("{4:2.8f}".format(23, "toto", 'Kiran', 'TN126BJ', 126.5783))


from collections import namedtuple

Baby = namedtuple('Baby', 'name,age,school,postcode')

baby = Baby('Rishi', '11', 'Barnies', 'TN126BJ')

print("Baby {0} is {1} months old, who goes to {2} nursery located at {3} Paddock Wood"
      .format(baby.name, baby.age, baby.school, baby.postcode))


def salutation(fn):
    def new(*args):
        return 'Mr ' + str(fn(*args))
    return new


@ salutation
def get_name(name):
    return name


def salute(x):
    return x


salute = salutation(salute)
print(salute('Kiran'))
print(get_name('Rishi'))


def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        func(x)
        print("After calling " + func.__name__)
    return function_wrapper


def foo(x):
    print("Hi, foo has been called with " + str(x))


print("We call foo before decoration:")
foo("Hi")

print("We now decorate foo with f:")
foo = our_decorator(foo)
print(foo.__name__)

print("We call foo after decoration:")
foo(42)
print(foo.__name__)

l1 = [1, 2, 3]
l2 = ['x', 'y', 'z']
print(l1, l2)
l2 = l1[:]
l2[1] = 'm'

print(l1, l2)

from collections import deque

d = deque(['tiger', 'elephant'])

d.append('cat')
d.append('mouse')
d.append('dog')

print(d.pop())
d.appendleft('cheetah')
print(d)


class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23


t = Test()
print(t.foo)
print(t.bar)
