import collections
import operator
import re

def mix(s1, s2):
  final_string = ""
  regex = re.compile('[^a-z]')

  text = dict()

  s1 = regex.sub('', s1)
  freq1 = collections.Counter(s1)

  freq1 = sorted(freq1.items(),key=operator.itemgetter(1))
  freq1=dict(freq1)
  # print(freq1)

  s2 = regex.sub('', s2)
  freq2 = collections.Counter(s2)

  freq2 = sorted(freq2.items(),key=operator.itemgetter(1))
  freq2=dict(freq2)
  # print(freq2)
  # print(dict(freq2))

  for k in freq1:
    for j in freq2:
      if k == j:
        if freq1[k] > freq2[j]:
          final_string = str(1) + ":" + k * freq1[k] + "/" + final_string
          text = dict([str(1), k * freq1[k]])
          # print("TEXT",text)
        elif freq1[k] < freq2[j]:
          final_string = str(2) + ":" + j * freq2[j] + "/" + final_string
          # text = dict([str(2), k * freq2[j]])
          # print(text)
        elif freq1[k] and freq2[j] > 1:
          final_string = final_string + "=" + ":" + j * freq2[j] + "/"
          # text = dict ([k, freq2[j] ])
          # print(text)
  final_string = final_string[:-1]
  return(final_string)


print(mix("Are they here", "yes, they are here"))
