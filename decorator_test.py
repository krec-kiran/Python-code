def p_decorate(func):
    def func_wrapper(*args, **kwargs):
        return "<p>{0}</p>".format(func(*args, **kwargs))
    return func_wrapper


def salutation(func):
    def func_wrapper(*args, **kwargs):
        return "Mr {0}".format(func(*args, **kwargs))
    return func_wrapper


def qualification(func):
    def func_wrapper(*args, **kwargs):
        return "{0} MBA".format(func(*args, **kwargs))
    return func_wrapper


class Person(object):

    def __init__(self):
        self.name = "John"
        self.family = "Doe"

    # @p_decorate
    @salutation
    @qualification
    def get_fullname(self):
        return self.name + " " + self.family

my_person = Person()
print(my_person.get_fullname())


# def polynomial_creator(a, b, c):
#     def polynomial(x):
#         return a * x**2 + b * x + c
#     return polynomial

# p1 = polynomial_creator(2, 3, -1)
# p2 = polynomial_creator(-1, 2, 1)

# for x in range(2, 10, 1):
#     print(x, p1(x), p2(x))
