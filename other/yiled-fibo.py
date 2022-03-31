def foo(n):
    a,b,c = 0,0,1
    while a < n:
        yield c
        b, c = c, b + c
        a += 1

for n in foo(5):
    print(n)


