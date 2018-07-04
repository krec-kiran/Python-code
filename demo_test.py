class Adder:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return 'Hello'

    def demo(self):
        return 'world'
    #
    # def __add__(self, another):
    #     return self.n+another.


test = Adder(5)
print(test(7))
print(callable(Adder))
print(test.demo())
