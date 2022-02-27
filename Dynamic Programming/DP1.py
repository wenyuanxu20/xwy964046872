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

    #print(res)

for i in range(1, n+1):
    for j in range(1, c+1):
        res[i][j]=res[i-1][j]
        if (j >= w[i - 1]):
            res[i][j] = max(res[i - 1][j - w[i - 1]] + v[i - 1], res[i-1][j]) #max(1500,0) 第一格是value = 0， 第二格1500


    print(res)

    print(max((max(res))))
