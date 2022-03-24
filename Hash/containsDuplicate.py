class Solution:
    def containsDuplicate(self, nums):
        return len(set(nums)) < len(nums)

nums  =  [1,2,3,1]
#s = Solution
print(Solution.containsDuplicate(Solution, nums))

# nums = [1,2,3,1]
#
# s = set(nums)
# print(s)
#
# print(len(set(nums)) < len(nums))