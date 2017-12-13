# a = [121, 19, 161, 19, 144, 19, 11]
# b = [14641, 121, 361, 25921, 361, 20736, 361]
# a = [11,11,121,19]
# b = [121,121,14641,361]
# a = [121, 144, 19, 161, 19, 144, 19, 11]
# b = [121, 14641, 20735, 361, 25921, 361, 20736, 361]
# a=[1,0,0]
# b=[1,0,0]
a=[2, 2, 3]
b= [4, 9, 9]

def are_they_same(a,b):
  if len(a)==0 or len(b)==0:
      return False
  index=0
  a_index=0
  while(len(a)>0):
    x=a[a_index]
    # print("x in begin",x)
    while(len(b)>0):
      if(b[index]!=x*x):
        index+=1
      else:
         b.remove(b[index])
         a.remove(x)
         # print("INDEX",a,b,index,len(b))
         index=0
         break
      if(index==len(b)):
       print("INDEX",a,b,index,len(b))
       return False
    a_index=0
  print("Index:",x,index,len(b))
  return True


print(are_they_same(a,b))

