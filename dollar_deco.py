def dollar(fn):
    def new(*args):
        return '$' + str(fn(*args))

    return new


def salutation(title):
    def salute(*args):
        return 'Mr'

    return salute

@dollar
@salutation
def price(amount, tax_rate):
    return amount + amount * tax_rate


print(price(100, 0.2))


def bold(f):
    def wrapper():
        return '<b>' + f() + '</b>'

    return wrapper


def italics(f):
    def wrapper():
        return '<i>' + f() + '</i>'

    return wrapper


@bold
@italics
def hello():
    return "hello world"


print(hello())
