import collections

def only_duplicates(string):
  text = list(string)
  freq=collections.Counter(text)
  for k in freq:
    if freq[k] < 2:
      text.remove(k)
  return(''.join(text))


print(only_duplicates("abccdefee"))
