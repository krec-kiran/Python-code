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


