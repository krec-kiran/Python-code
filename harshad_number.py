class Harshad:
    @staticmethod
    def is_valid(number):
        n = [int(n) for n in str(number)]
        if number != 0 and number % sum(n) == 0:
            return True
        else:
            return False

    @staticmethod
    def get_next(number):
        number += 1
        while not Harshad.is_valid(number):
            number += 1
        return number

    @staticmethod
    def get_series(count, start=0):
        result = []
        i = 0
        val = start
        while i < count:
            val = Harshad.get_next(start)
            result.append(val)
            start = val
            i += 1
        return result


print(Harshad.is_valid(19))
print(Harshad.get_next(0))
print(Harshad.get_series(3, 1000))
