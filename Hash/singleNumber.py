class Solution:
    def find_single(nums):
        s = set(nums)
        #print(s)
        for i in s:
            if nums.count(i) == 1:
                return i


nums = [4, 1, 2, 1, 2, 7]
x = Solution.find_single(nums)
print(x)