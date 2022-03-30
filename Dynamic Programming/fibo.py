def fibo(n):
    if n < 2:
        return n

    a,b,c = 0, 0, 1
    for i in range(2, n+1):
        print(i)
        a,b = b,c
        c = a+b

    return c

# 1 1 2 3 5 8

print(fibo(3))