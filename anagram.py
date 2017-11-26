# source = input("Enter the first string")
# dest =  input("Enter the second string")

# if(''.join(sorted(source))==''.join(sorted(dest))):
#   print("Anagram")
# else:
#   print("Not an Anagram")

source='parliament'
dest="partial men"
i=0
j=0

source=source.replace(" ","")
dest=dest.replace(" ","")

print("Source",source,"Dest",dest)

if len(source)!= len(dest):
  print("Strings are not of equal length")
  exit()


for x in source:
  i+=1
  j=0
  for y in dest:
    j+=1
    if x==y:
      break
    elif x!=y and len(source)==j:
      print("Not an Anagram!\n")
      exit()
    elif len(source)!=j:
      continue

print("Yes,it is an Anagram!\n")

