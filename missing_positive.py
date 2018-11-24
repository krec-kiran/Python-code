class Solution:
    def findPositive(nums):
        if not nums:
            return
        small = max([x for x in nums if x < 0])
        if small != -1:
            small = min([x for x in nums if x > 0])
        for i in range(len(nums)):
            if small not in nums and small > 0:
                return small
            else:
                small += 1


print(Solution.findPositive([2, 3, 7, 6, 8, -1, -10, 15]))
print(Solution.findPositive([2, 3, -7, 6, 8, 1, -10, 15]))
print(Solution.findPositive([1, 1, 0, -1, -2]))
