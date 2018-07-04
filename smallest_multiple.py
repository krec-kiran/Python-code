# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

nums = [7, 11, 12, 13, 15, 16, 17, 18, 19, 20]
message = "The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is: "

for numb in range(2521, 1000000000):
    for i in nums:
        if numb % i != 0:
            break
        if i == nums[9]:
            print(message, numb)
            exit()
