from collections import namedtuple

# Named tuples allow members to be accessed by name instead of index as in regular tuples
# return a subclass of type name

Car = namedtuple('Car','color mileage model')

my_car = Car('red',4512,'Ford Fiesta')

print(my_car.color)
print(my_car)
