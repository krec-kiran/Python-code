'''A friend of mine takes a sequence of numbers from 1 to n (where n > 0).
Within that sequence, he chooses two numbers, a and b.
He says that the product of a and b should be equal to the sum of all numbers in the sequence, excluding a and b.
Given a number n, could you tell me the numbers he excluded from the sequence?

removNb(26) should return [(15, 21), (21, 15)] '''

# def removNb(n):
#   original_elements=[x for x in range(n)]
#   original_elements=original_elements[2:]
#   test_elements=[k for k in range(n)]
#   test_elements=test_elements[2:]
#   toto=sum(range(n+1))
#   result=[]
#   new_elements=original_elements
#   for x in new_elements:
#     # new_elements.remove(x)
#     # print(new_elements)
#     test_elements=test_elements[1:]
#     for y in test_elements:
#       # print(test_elements)
#       # print("X,Y",x,y)
#       if x*y==(toto-(x+y)):
#         tup1=(x,y)
#         tup2=(y,x)
#         result.append(tup1)
#         result.append(tup2)
#         return(result)
#     # new_elements=test_elements
#     # print("After Assign",new_elements)

#   return(result)

def removNb(n):
  elements=[x for x in range(n)]
  elements=elements[2:]
  toto=sum(range(n+1))
  result=[]
  for x in elements:
    test_elements=elements[1:]
    for y in test_elements:
      if x*y==(toto-(x+y)):
        tup1=(x,y)
        tup2=(y,x)
        result.append(tup1)
        result.append(tup2)
        return(result)
  return(result)


# def removNb(n):
#   elements=[x for x in range(n)]
#   elements=elements[2:]
#   toto=sum(range(n+1))
#   result=[]
#   count=0
#   # for x in elements:
#   x=elements[count]
#   count+=1
#   test_elements=elements[1:]
#   print(x,test_elements)
#   for y in test_elements:
#     print(y)
#     if x*y==(toto-(x+y)):
#       tup1=(x,y)
#       tup2=(y,x)
#       result.append(tup1)
#       result.append(tup2)
#       return(result)
#   if(elements is None):
#     return(result)


print(removNb(10))
print(removNb(67))
print(removNb(197))
print(removNb(201))
print(removNb(3006))
print(removNb(10045))
print(removNb(15045))


