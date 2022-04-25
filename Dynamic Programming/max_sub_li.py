li = [-2,1,-3,4,-1,2,1,-5,4]

x = sum(li)

print(x)

dp = [0 for _ in range(len(li))]  #用来存储结果

dp[0] = li[0]


#dp[i]: dp[i-1] > 0: dp[i] = dp [i-1] + li[i]  否则dp[i] = li[i]
for i in range(1,len(li)):
    if dp[i - 1] >= 0:
        dp[i] = dp[i - 1] + li[i]
    else:
        dp[i] = li[i]

print(max(dp))
