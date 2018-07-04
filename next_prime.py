def isPrime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


number = int(input("Enter your number "))
number += 1
while(isPrime(number) is False):
    number += 1

print("The next prime number is ", number)
