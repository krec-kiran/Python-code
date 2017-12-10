# a=["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"]
# starr=["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"]
k=15
# starr=["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"]
# starr=["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"]
# starr=["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"]
starr=["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"]
# k=0
# long_index=a.index(max(a,key=len))
# print(long_index)
# print("LENGTH:",len(a))
# print(a[long_index])
# long_consec_string = a[long_index]
# count=1

# if k==0:
#   print('')

# if long_index < len(a)-1:
#   if len(a[long_index+1])>len(a[long_index-1]):
#     while count < k:
#      long_consec_string+=a[long_index+count]
#      count+=1
#   else:
#     while count < k:
#       long_consec_string=a[long_index-count]+long_consec_string
#       count+=1


# print(long_consec_string)

def longest_consec(strarr, k):
  if k<=0 or k>len(strarr):
      return ''
  if strarr:
        long_index=strarr.index(max(strarr,key=len))
  else:
        return ''
  long_consec_string = strarr[long_index]
  count=1
  # print("Length:",len(strarr))
  # print("Long index:",long_index)
  if long_index < len(strarr)-1:
    if len(strarr[long_index+1])>len(strarr[long_index-1]):
      while count < k and long_index+count <len(strarr):
        long_consec_string+=strarr[long_index+count]
        count+=1
    else:
      while long_index>0:
        long_consec_string=strarr[long_index-1]+long_consec_string
        long_index-=1
  else:
      while count < k:
        long_consec_string=strarr[long_index-count]+long_consec_string
        count+=1
  return long_consec_string



print(longest_consec(starr,k))
