#triangle = [[2], [3,4], [6,5,7], [4,1,8,3]]
#triangle = [[2], [3,4], [6,5,1], [4,1,8,3], [9,2,7,2,9]]
triangle = [[2], [3, 4], [5, 6, 7]]
path = 0

print(triangle[-1])

for i in range(len(triangle)-2, -1, -1):  # 倒着遍历行
    print(triangle[i])
    for j in range(len(triangle[i])):  # 遍历每行各位置
        triangle[i][j] = triangle[i][j] + min(triangle[i+1][j], triangle[i+1][j+1])   #

print(triangle[0][0])

