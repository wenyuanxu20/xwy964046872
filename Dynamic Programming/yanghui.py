# 3-29

n = 5

l = []

for i in range(1, n+1):
    l.append([1]*i)

for i in range(2, n):
    for j in range(1, len(l[i]) - 1):
        l[i][j] = l[i-1][j-1] + l[i-1][j]

print(l) # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]