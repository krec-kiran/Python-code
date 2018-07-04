# 2(a3(b)) = 'abbbabbb'
# s = '3(d(a)2bc)'
s = '3(ab)'
s = s.replace('(', '')
s = s.replace(')', '')
print(s)

i = len(s) - 1
dummy = ''
while(i >= 0):
    if s[i].isalpha():
        dummy = s[i] + dummy
    if s[i].isdigit():
        dummy = dummy * int(s[i])
    print(dummy)
    i = i - 1

print(dummy)
