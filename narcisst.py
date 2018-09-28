value = 122

print(len(str(value)))
toto = 0
for i in str(value):
    toto += pow(int(i), len(str(value)))

if toto == value:
    print('True')
else:
    print('False')
