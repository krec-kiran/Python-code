import collections
import re


def mix(s1, s2):
  final_string = ""
  regex = re.compile('[^a-z]')

  s1 = regex.sub('', s1)
  freq1 = collections.Counter(s1)

  s2 = regex.sub('', s2)
  freq2 = collections.Counter(s2)

  for k in freq1:
    for j in freq2:
      if k == j:
        if freq1[k] > freq2[j]:
          final_string = final_string + str(1) + ":" + k * freq1[k] + "/"
        elif freq1[k] < freq2[j]:
          final_string = final_string + str(2) + ":" + j * freq2[j] + "/"
        elif freq1[k] and freq2[j] > 1:
          final_string = final_string + "=" + ":" + j * freq2[j] + "/"
  final_string = final_string[:-1]
  return(final_string)


print(mix("Are they here", "yes, they are here"))
