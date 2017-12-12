n=1234
def countBits(n):
  n=bin(n)
  n=list(n[2:])
  b=[x for x in n if x=='1']
  b=len(b)
  print(b)


def remove_char(s):
  s=s[1:-1]
  print(s)

talk="puke Love hiccup hiccup most, puke puke puke Trust hiccup hiccup     puke none!"
s="bangalore"

def wdm(talk):
  words=['puke','hiccup']
  text=""
  talk=talk.split()
  print(talk)
  for x in talk:
    if x not in words:
      text=text+" "+x
  text=text.strip()
  print(text)


countBits(456)
remove_char(s)
wdm(talk)
