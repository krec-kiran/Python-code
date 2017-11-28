''' Trans bought a calculator at creatnx's store. Unfortunately, it is fake.
It has many bugs. One of them is adding two numbers without carrying.
Example expression: 12 + 9 will have result 11 in his calculator.
Given an expression in the form a + b, please output result from that calculator.'''

val1=input("Enter input val 1\t")
val2=input("Enter input val 2\t")

val1=[int(i) for i in str(val1)]
val2=[int(i) for i in str(val2)]

result=[]
soln=[]

if len(val1)<len(val2):
  i=len(val1)
  while i<len(val2):
    val1.insert(0,0)
    i+=1
else:
  i=len(val2)
  while i<len(val1):
    val2.insert(0,0)
    i+=1

result=list(zip(val1,val2))

for i in range(len(result)):
  soln.append(int((result[i][0]+result[i][1])%10))

print(''.join(map(str,soln)))

