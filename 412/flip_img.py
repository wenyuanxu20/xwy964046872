matrix = [[1,2,3],[4,5,6],[7,8,9]]
# for i in matrix:
#     print(i)


n = len(matrix)

# 水平上下翻转
for i in range(n // 2):
    for j in range(n):
        matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]

for i in matrix:
    print(i)


# 对角线翻转
for i in range(n):
    for j in range(i):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

print('-----')

for i in matrix:
    print(i)