sumOfSquares = 0
squareOfSum = 0
for i in range(1, 11):
    sumOfSquares += (i * i)
    squareOfSum += i
print(squareOfSum)
print("Differece is", squareOfSum**2 - sumOfSquares)
