n = 499502

count = 0
for i in range(1, n + 1):
    count += i
    if count > n:
        break
print(i)
