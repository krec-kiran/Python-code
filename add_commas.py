n = 1000000000.234758

n = round(n, 3)
print(n)
n = str(n).split('.')

whole = n[0]

result = ''
start = 0
end = 0
for i in range(len(whole)):
    if (i + 1) % 3 == 0:
        end = i + 1
        result += whole[start:end] + ','
        start = end
print(result.strip(',') + '.' + n[1])
