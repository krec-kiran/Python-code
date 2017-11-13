def checkNumber(number):
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")

for i in range(1, 10):
    checkNumber(i)
