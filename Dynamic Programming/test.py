# coding=utf-8
#

nums = [1,2,3,4]

# running_sum = []
# res = []
#
# for i in range(len(nums)):
#     running_sum.append(nums[i])
#     x = sum(running_sum)
#     res.append(x)
# print(running_sum)
# print(res)


for i in range(1,len(nums)):
    nums[i] += nums[i-1]

print(nums)
