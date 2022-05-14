def minimumTotal(triangle):
    n = len(triangle)
    f = [[0] * n for _ in range(n)]
    f[0][0] = triangle[0][0]
    print(f)

    for i in range(1, n):
        f[i][0] = f[i - 1][0] + triangle[i][0]
        for j in range(1, i):
            f[i][j] = min(f[i - 1][j - 1], f[i - 1][j]) + triangle[i][j]
        f[i][i] = f[i - 1][i - 1] + triangle[i][i]

    return min(f[n - 1])



triangle = [[2], [3,4], [6,5,1], [4,1,8,3], [9,2,7,2,9]]

print(minimumTotal(triangle))
