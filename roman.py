numerals = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X',
            50: 'L', 100: 'C', 500: 'D'}

counter = [0] * 5

number = int(input("Enter the number "))

#  initialise roman and value (to store the roman number as it forms)

roman = value = ''

if number >= 1000:
    counter.insert(0, int(number / 1000))
    number = number % 1000

if number >= 500 and number < 1000:
    counter.insert(1, int(number / 500))
    number = number % 500

if number >= 100 and  number < 500:
    counter.insert(2, int(number / 100))
    number = number % 100

if number >= 50 and number < 100:
    counter.insert(3, int(number / 50))
    number = number % 50

if number >= 10 and number < 50:
    counter.insert(4, int(number / 10))
    number = number % 10

number = number % 10
if number != 0:
    roman = numerals[number]
    print(roman)

print("Roman Weightage Counte", counter)

for i in range(len(counter)):
    if counter[i] and i == 0:
        value = value + ''.join(counter[0] * ['M'])
    if counter[i] and i == 1:
        value = value + ''.join(counter[1] * ['D'])
    if counter[i] and i == 2:
        value = value + ''.join(counter[2] * ['C'])
    if counter[i] and i == 3:
        value = value + ''.join(counter[3] * ['L'])
    if counter[i] and i == 4:
        value = value + ''.join(counter[4] * ['X'])

print("ROMAN NUMBER IS", value+roman)


# def f(x):
#   for i in range(len(counter)):
#     if counter[i]:
#       return {
#           0: value = value + ''.join(counter[0] * ['D']),
#           1: value + ''.join(counter[1] * ['C']),
#           2: value = value + ''.join(counter[2] * ['L']),
#           3: value = value + ''.join(counter[3] * ['X']) + roman
#       }.get(x)




