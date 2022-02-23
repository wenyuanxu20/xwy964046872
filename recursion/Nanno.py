def Hanno(n,a,b,c): # n个盘子，从a经过b移动到c
    if  n > 0:
        Hanno(n-1,a,c,b) #n-1个盘子，从a经过c移动到b
        print('moving from %s to %s' %(a,c)) #第n个盘子（最底下最大一个），从a移动到c
        Hanno(n-1,b,a,c) #n-1个盘子，从b经过a移动到c

Hanno(2,'A', 'B', 'C')