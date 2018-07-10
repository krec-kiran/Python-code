beach = 'gOfIshsunesunFiSh'
beach = beach.lower()
words = ['sand', 'water', 'fish', 'sun']
count = 0

for w in words:
    if w in beach:
        count += beach.count(w)
print(count)
