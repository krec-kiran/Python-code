# function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

a=[1,2,'a','b','1']

k=[x for x in a if type(x) == type(1)]
