class Solution:
    def find_intersection(self, num1, num2):
#        res = []
        set1 = set(num1)
        set2 = set(num2)
        # for i in set1:
        #     if i in set2:
        #         res.append(i)

        return list(set1 & set2)




num1 = [1,2]
num2 = [2,3]


x = Solution.find_intersection(Solution,num1,num2)
print(x)