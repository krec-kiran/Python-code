# source = input("Enter the first string")
# dest =  input("Enter the second string")

# if(''.join(sorted(source))==''.join(sorted(dest))):
#   print("Anagram")
# else:
#   print("Not an Anagram")

source='Clint Eastwood'
dest="Old west Action"

source=source.replace(" ","")
dest=dest.replace(" ","")

if len(source)!= len(dest):
  print("Not an Anagram")
  exit()

source=''.join(set(source.lower()))
dest=''.join(set(dest.lower()))


# source=''.join(set(source.lower()))
# dest=''.join(set(dest.lower()))

if len(source)!= len(dest):
  print("Not an Anagram")
  exit()

for x in source:
  j=0
  for y in dest:
    j+=1
    if x==y:
      break
    elif x!=y and len(source)==j:
      print("Not an Anagram!\n")
      exit()

print("Yes,it is an Anagram!\n")

from itertools import permutations
s="rat"
perms = [''.join(x) for x in permutations(s)]
print("Angrams of strings are",perms)

# target=list(permutations(s))
# for item in target:
#   print(''.join(item),)


