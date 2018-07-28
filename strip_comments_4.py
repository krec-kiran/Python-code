s = 'Hello world ! Kiran in Bangalore # Hello I am here* Kiran'
sub = '!'
# result = ''
#
# print(list(sub))
#
#
# after = s
#
# print(list(after))
# print(list(set(after) & set(list(sub))))
#
# i = 0
# # while len(after) > 0:
# while(i < 3):
#     print('I', i)
#     if len(list(set(list(after)) & set(list(sub)))) == 0:
#         print('blank')
#         exit()
#     k = after.find(sub)
#     print("index", k)
#     before = s[:k]
#     k = k + 1
#     after = s[k:]
#     print("After", after)
#     result = before + after
#     print(result)
#     i += 1

# s = 'GATTACA'
k = [i for i, char in enumerate(s) if char == "*"]
print(k)
