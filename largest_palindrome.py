# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

message = "The largest palindrome made from the product of two 3-digit numbers:"
big = 0
for i in range(100, 1000):
    for j in range(i + 1, 1000):
        val = i * j
        if str(val) == ''.join(reversed(str(val))):
            if val > big:
                big = val
print(message, big)
