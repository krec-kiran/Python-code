def accum(s):
  i=1
  s=list(s)
  out=s[0]
  s=s[1:]
  for x in s:
    out=out+"-"+x.capitalize()
    if x.upper():
      out+=(x.lower()*i)
    i+=1
  print(out)

s='ZpglnRxqenU'
accum(s)
