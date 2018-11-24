class Solution:
    def findPositive(nums):
        if not nums:
            return
        small = min([x > 0 for x in nums])
        for i in range(len(nums)):
            if small not in nums and small > 0:
                return small
            else:
                small += 1


print(Solution.findPositive([2, 3, 7, 6, 8, -1, -10, 15]))
