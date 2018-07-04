
# In this kata, your task is to create a regular expression capable of evaluating binary strings (strings with only 1s and 0s) and determining whether the given string represents a number divisible by 3.
#
# Take into account that:
#
# An empty string might be evaluated to true (it's not going to be tested, so you don't need to worry about it - unless you want)
# The input should consist only of binary digits - no spaces, other digits, alphanumeric characters, etc.
# There might be leading 0s.
# 5kyu

val = '1100'


def divideByThreeCheck(val):
    if(int(val, base=2) % 3) == 0:
        print("Divisible by 3")
    else:
        print('NOT Divisible by 3')


divideByThreeCheck(val)
