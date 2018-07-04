def f(x):
    print("X is:", x)

    def g(y):
        print("Y is:", y)
        return y + x + 3
    return g

nf1 = f(1)
# nf2 = f(3)

print(nf1(3))
# print(nf2(1))

def square(x):
    def cube(y):
        return (y * y * y + x)
    return cube


def square(x):
    def cube(y):
        return (y * y * y + x)
    return cube

number = square(10)

print(number(5))


def greet(name):
    return "Hello " + name


def call_func(func):
    other_name = "John"
    return func(other_name)

print(call_func(greet))


def p_decorate(func):
    def func_wrapper(name):
        return "<p>{0}</p>".format(func(name))
    return func_wrapper


def strong_decorate(func):
    def func_wrapper(name):
        return "<strong>{0}</strong>".format(func(name))
    return func_wrapper


def div_decorate(func):
    def func_wrapper(name):
        return "<div>{0}</div>".format(func(name))
    return func_wrapper


@div_decorate
@p_decorate
@strong_decorate
def get_text(name):
    return "lorem ipsum, {0} dolor sit amet".format(name)


# my_get_text = p_decorate(get_text)

print(get_text("John"))


def tags(tag_name):
    def tags_decorator(func):
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator


@tags("div")
@tags("p")
@tags("strong")
def get_text(name):
    return "Hello " + name

print(get_text("John"))
