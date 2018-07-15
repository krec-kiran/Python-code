numbers = [2, 4, 6, 8, 10, 3]

even = [x for x in numbers if x % 2 == 0]
odd = [x for x in numbers if x % 2 != 0]

if len(even) == 1:
    print(even[0])
else:
    print(odd[0])
