import re

# str1='RGRGR'
# str2='GRGRG'
# RRG RGR - 5
# GGR GRG - 3

# 'RGRGGR'
# str1='RRRGRGRGRGRGRGRGRGGG'
str1='RGRGRGRGRGRGRGRRGGRG'
# str1='RRGGGR'
l1=list(str1)
cost=0
x=0
y=1
y_pos=0

print("ORIGINAL LIST",l1)

for x in range(len(l1)-1):
 x_pos=x
 print(x)
 if x!=len(l1)-1 and l1[x]==l1[x+1]:
   if l1[x]=='R' and y<len(l1)-1:
      y_pos=y
      while(l1[y]!='G' and y<len(l1)-1):
        y+=1
      cost+=5
      l1[y_pos],l1[y]=l1[y],l1[y_pos]
      print("LIST-1, cost",l1, cost)
      x=x_pos+2
      y=x+1
      print("X,Y,LIST",x,y,l1,l1[x],l1[y])
 if x!=len(l1)-1 and l1[x]==l1[x+1]:
   if l1[x]=='G' and y<len(l1)-1:
      y_pos=y
      while(l1[y]!='R' and y<len(l1)-1):
        y+=1
      cost+=3
      l1[y_pos],l1[y]=l1[y],l1[y_pos]
      print("LIST-2, cost",l1, cost)
      x=x_pos+2
      y=x+1

print("Cost is:",cost)
print("FINAL LIST",l1)


