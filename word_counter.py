counter=dict()
text='''How can mirrors be real if our eyes aren't real How can mirrors be real if our eyes aren't real
How can mirrors be real if our eyes aren't real How can mirrors be real our eyes aren't real'''

for word in text.split():
  counter[word]=text.count(word)

print(counter)


