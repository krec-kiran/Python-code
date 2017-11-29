'''The Chef had a box with N numbers arranged inside it: A1, A2, ..., AN.
He also had the number N at the front, so that he knows how many numbers are in it.
That is, the box actually contains N+1 numbers. But in his excitement due the ongoing IOI,
he started dancing with the box in his pocket, and the N+1 numbers got jumbled up. So now,
he no longer knows which of the N+1 numbers is N, and which the actual numbers are.
He wants to find the largest of the N numbers. Help him find this.'''

# a=[1,2,1]
# a=[3,1,2,8]
a=[1,5,1,4,3,2,9,8,17,16,12,19]

count=len(a)-1

# b=list(a)
# [b.remove(count)]

b=[x for x in a if x!=count]
print(max(b))

