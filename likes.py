names=['Alex', 'Jacob', 'Mark', 'Max']
def likes(names):
  text=""
  tag="like this"
  length=len(names)

  if(length==0):
      return("no one likes this")
  if(length==1):
      return(names[0] + " likes this")
  else:
    i=0
    for x in names:
        i+=1
        if x==names[length-1]:
          text+="and "+x + " "
        elif x==names[length-2]:
          text+=x+" "
        elif length>2:
          if i>=2:
            text+=x+ " and "+ str(length-2) + " others "
            break
          text+=x+", "


  return(text+tag)


print(likes(names))
