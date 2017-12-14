# namelist= [ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]
# namelist=[ {'name': 'Bart'} ]
# namelist=[]
namelist=[{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]

names = [li['name'] for li in namelist ]

def namelisting(namelist):
  s=''
  names = [li['name'] for li in namelist ]
  if len(names) > 1:
    s="'",", ".join(names[:-1])," & "," ".join(names[-1:]),"'"
    return ''.join(s)
  elif len(names)==1:
    s="'","".join(names),"'"
    return ''.join(s)
  else:
    return s


print(namelisting(namelist))

# if len(names) > 1:
#   print("'",", ".join(names[:-1]),"and","".join(names[-1:]),"'")
# else:
#   print("'","".join(names),"'")



