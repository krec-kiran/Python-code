# works for these cases
a=123567
c=599600601602
d=9899101102
e=900001900002900004900005900006
g=900001900002900004900005900006

# does not work!

f=99991000110002
b=899091939495


def missing(s):
  numb_string = str(s)
  length = len(numb_string)
  k=1
  while(k < length):
    if length%k == 0:
      index = 0
      start = 0
      end = k
      if (int(numb_string[start + k:end + k]) - int(numb_string[start:end])) == 1:
        digit = int(numb_string[start:end])
        while end < length:
          digit+= 1
          start+= k
          end+= k
          if digit!=int(numb_string[start:end]):
            return digit
        return -1
    k+=1
    if k==length:
      return "-1"

print(missing(f))

