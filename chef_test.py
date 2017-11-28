# n=[-3,7,12,0,5,8,4,2,19]

'''Even though it was a little unexpected, Chef did it! He has finally opened a new restaurant!

As you all know, to make everything go well, Chef needs employees (co-chefs if you might say). Because Chef is a perfectionist,
he planned to employ only chefs who are good at competitive progeamming. Hence, Chef asked for help from his friends Shahhoud and Said.
Knowing that many people (such as Ahmad, Nour, Majd and Joud) will apply for the job, they decided to choose only the best appliers.

As the day of the employment came, people lined up in front of the restaurant applying for the job. Before accepting any appliers,
Shahhoud and Said decided to make them answer a simple question, in order to determine which of them better deserves the job.

Given an array of N elements A1, A2, ..., AN, each applier was asked to insert any K integers he wants to this array. Eventually,
each applier will be asked to write down the median among all the elements in his resulting array.
Many appliers asked for your help to determine what is the greatest median they can get after inserting any K elements they want? '''

n=[6,1,1,1,1,2,4,9]

count=len(n)

k=5
m=[30,10,0,11,19]

n=sorted(n+m)

print("Sorted Array:",n)
median=int((count+k)/2)

# print(median)

print("The maximum median value to achieve is:",n[median])



# for x in n:
#   for y in n:
#     if (x*y)==12:
#       print(x,y)
