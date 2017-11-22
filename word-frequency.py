ss = """I figured it out
I figured it out from black and white
Seconds and hours
Maybe they had to take some time"""

words=ss.split()

print(words)

d={}.fromkeys(words,0)

print(d)

for word in words:
  d[word]+=1;

print(d)
