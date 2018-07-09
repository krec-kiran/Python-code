s = ["turns", "out", "random", "test", "cases", "are",
     "easier", "than", "writing", "out", "basic", "ones"]

s = sorted(s)
word = s.pop(0)
result = ''

for i in range(len(word) - 1):
    result += word[i] + '***'
result += word[len(word) - 1]
print(result)
