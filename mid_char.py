text = "ABC"

length = len(text)
if length % 2 == 0:
    mid = int(length / 2)
    print(text[mid - 1:mid + 1])
else:
    mid = int((length - 1) / 2)
    print(text[mid])

# def mystery(n):
#     print(n)
#     if not int(n):
#       return -1

# def wrap_mystery(n):
#     return mystery(n)


# print(wrap_mystery(2.4))
