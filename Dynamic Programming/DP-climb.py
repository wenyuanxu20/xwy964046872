
# 第n个台阶只能从第n-1或者n-2个上来。到第n-1个台阶的走法 + 第n-2个台阶的走法 = 到第n个台阶的走法，已经知道了第1个和第2个台阶的走法，一路加上去。
class Solution:
    def climb(self, n):
        a = 1
        b = 2

        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            for i in range(2, n):

                temp = a
                a = b
                b = temp + b
                i += 1

        return b


s = Solution.climb(Solution,4)
print(s)