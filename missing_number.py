a=123567
b=899091939495
c=599600601602
d=9899101102

numb_string = str(d)

# print(len(str(a)))
length = len(numb_string)
print(length)
k=1
# print(numb_string[1:2])


def check(k):
  index=0
  start=0
  end=k
  # print("ENTERING")
  # print("left digit",numb_string[start:end])
  # print("right digit",numb_string[start+k:end+k])
  if ( int(numb_string[start+k:end+k]) - int(numb_string[start:end] )) == 1:
    digit=int(numb_string[start:end])
    print("DIGIT-BEFORE",digit)
    print(end)
    while end<length:
      digit+=1
      start+=k
      end+=k
      # if (int(numb_string[start+k:end+k]) - int(numb_string[start:end] )) == 1:
      if digit!=int(numb_string[start:end]):
          print("Missing digit",digit)
          # print(numb_string[start:end])
          # print(numb_string[start+k:end+k])
          exit()
          # print(int(numb_string[start:end]))
    print("No number missing -1")
    exit()      # exit()
    # print("-1")



while(k<length):
  if length%k==0:
    check(k)
  k+=1
  if k==length:
    print("while -1")


