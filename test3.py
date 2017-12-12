def missing(s):
  numb_string = str(s)
  length = len(numb_string)
  k=1
  numbers=[]
  while(k < length):
    # if length%k == 0:
      # check(k, numb_string, length)
      index = 0
      start = 0
      end = k
      if (int(numb_string[start + k:end + k]) - int(numb_string[start:end])) == 1:
        digit = int(numb_string[start:end])
        print(digit)
        numbers.append(digit)
        while end < length:
          if digit%9==0:
            k+=1
          digit+= 1
          start=end
          end+=k
          numbers.append(int(numb_string[start:end]))
          print("number",int(numb_string[start + k:end + k]))
      k+=1
      start=0
      end=k
      print(start,end,k)
      print("K value:",k)
      if numbers:
       print(numbers)
      numbers=[]
      k+=1


print(missing("979899100101102"))



a=[0,1,2,3,5,6]
b=[0,1,2,3,4,5]

print(set(b) - set(a))

# special case: 899091939495
# special case: 979899100101102
