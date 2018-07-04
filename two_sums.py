nums = [3,8,3,2,7]
initial_nums = nums
target=15
initial_target = target

def twosums(nums,target):
  toto=0
  i=0
  # nums.sort()
  while toto <= target:
    toto+= nums[i]
    target-= nums[i]
    print(nums[i])
    print(toto,target)
    nums.pop(i)
    print(nums)
    if target in nums:
      return(i,nums.index(target))
      break
    else:
      i+=1
      toto=0
      target=initial_target
      nums=initial_nums
      print("NUMS",nums)

print("The traget",target,"can be achieved by these two indexes in array nums:",twosums(nums,target))

