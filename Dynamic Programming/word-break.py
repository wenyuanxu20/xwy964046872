dict = ['leet','code']
s = 'leetcode'
n = len(s)
dp = [False] * (n+1)
dp[0] = True
print(dp)

for i in range(n):
    for j in range(i+1, n+1):
        if (dp[i] and (s[i:j] in dict)):
            dp[j] = True

print(dp[-1])

