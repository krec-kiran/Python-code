def p_decorate(func):
    def func_wrapper(*args):
        return "<p>{0}</p>".format(func(*args))
    return func_wrapper


def salutation(func):
    def func_wrapper(*args):
        return "Mr {0}".format(func(*args))
    return func_wrapper


def qualification(f):
    def func_wrapper(*args):
        return "{0} MBA".format(f(*args))
    return func_wrapper


class Person(object):

    def __init__(self):
        self.name = "John"
        self.family = "Doe"
        self.city = "London"

    # @p_decorate
    @salutation
    @qualification
    def get_fullname(self):
        return self.name + " " + self.family + " " + self.city

my_person = Person()
print(my_person.get_fullname())

# # example to understand decorator

# def get_text(name):
#    return "lorem ipsum, {0} dolor sit amet".format(name)

# def p_decorate(func):
#    def func_wrapper(name):
#        return "<p>{0}</p>".format(func(name))
#    return func_wrapper

# my_get_text = p_decorate(get_text)

# print my_get_text("John")

# # <p>Outputs lorem ipsum, John dolor sit amet</p>

