x = [0]
n = 10
HB = 0

for i in range(1, n + 1):
    if i & (i - 1) == 0:
        HB = i
    print(x[i - HB])
    x.append(x[i - HB] + 1)

print(x)