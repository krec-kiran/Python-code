# source = input("Enter the first string")
# dest =  input("Enter the second string")

# if(''.join(sorted(source))==''.join(sorted(dest))):
#   print("Anagram")
# else:
#   print("Not an Anagram")

source='Clint Easwtood'
dest="Old west Action"

source=''.join(set(source.replace(" ","").lower()))
dest=''.join(set(dest.replace(" ","").lower()))

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

