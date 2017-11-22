# pblm - 9 - captialize the input

# text = input("Enter your sentence...\n")

# print(str(text).upper())

# text = input("Enter your sentence...\n")

# pblm - 13 find the number of letters / digits in a given input

text="hello world! 123"
letter=0
digit=0

for char in text:
  if(char.isalpha()):
    letter+=1
  elif(char.isdigit()):
    digit+=1

print("letters:",letter,"digits:",digit)


