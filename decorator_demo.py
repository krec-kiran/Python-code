def bold(f):
    def wrapper(*args):
        return '<b>' + f(*args).upper() + '</b>'

    return wrapper


def italics(f):
    def wrapper(*args):
        return '<i>' + str(f(*args)).title() + '</i>'

    return wrapper


@italics
@bold
def hello(string):
    return string


print(hello('I am in London'))
