'''You are going to be given an array of integers. Your job is to take that array and find an index N
where the sum of the integers to the left of N is equal to the sum of the integers to the right of N.
If there is no index that would make this happen, return -1.'''


a = [20,10,-80,10,10,15,35]

def equal_check(a):
  for i in range(len(a)):
    right_side = a[i + 1:]
    left_side = a[0:i]
    if sum(left_side) == sum(right_side):
      return i

  return -1

print(equal_check(a))

