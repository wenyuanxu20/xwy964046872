# coding=utf-8
#


c = 4  # bag capacity
n = 3  # item num
v = [1500, 3000, 2000]  # value
w = [1, 4, 3]  # weight

res = [[0 for j in range(c+1)]for i in range(n+1)]

for j in range(c+1):
    # 第0行全部赋值为0，物品编号从1开始.为了下面赋值方便
    res[0][j] = 0


print(res)

i = 1
j = 1

res[i][j]=res[i-1][j]

print(res)