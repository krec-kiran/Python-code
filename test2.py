def missing(s):
  numb_string = str(s)
  length = len(numb_string)
  k=1
  while(k < length):
    if length%k == 0:
      # check(k, numb_string, length)
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
      return -1

print(missing("998999100010011003"))
