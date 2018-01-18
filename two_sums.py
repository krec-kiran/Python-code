nums = [2,7,11,13,15]
target=20
initial_target = target
indexes=[]


def twosums(nums,target):
  toto=0
  i=0
  nums.sort()
  while toto < target:
    toto+= nums[i]
    target-= nums[i]
    if target in nums:
      return(i,nums.index(target))
      break
    else:
      i+=1
      toto=0
      target=initial_target

print("The traget",target,"can be achieved by these two indexes in array nums:",twosums(nums,target))

