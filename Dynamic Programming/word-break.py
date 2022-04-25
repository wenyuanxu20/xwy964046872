dict = ['leet','code']
s = 'leetcode'
n = len(s)
dp = [False] * (n+1)
dp[0] = True
print(dp)
times = 0

for i in range(n):
    for j in range(i+1, n+1):
        times += 1
        if (dp[i] and (s[i:j] in dict)):
            dp[j] = True
            i = j

print(dp[-1])
print(times)
