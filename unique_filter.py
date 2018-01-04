import collections

def only_duplicates(string):
  text = list(string)
  dummy = text
  freq=collections.Counter(text)
  for k in freq:
    if freq[k] < 2:
      dummy.remove(k)
  return(''.join(dummy))



print(only_duplicates("abccdefee"))
