n = '1234678'
print(n[0:1])
count = 2
toto = int(len(n) / count)
start = 0
end = count
vals = []
for i in range(1, toto + 1):
    vals.append(n[start:end])
    vals.append(n[end:])
    start += count
    end += count
print(vals)
