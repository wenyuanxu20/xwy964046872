import random
import numpy as np

def bubble_sort(li):
    for i in range(len(li) - 1): #一共排（n-1）次
        for j in range(len(li) - i - 1):  #ex：第二轮：已经有2个数在最上边（0，1两轮结束后），无序区范围是0-6, 6 = 9-2-1 = len(li) - i - 1
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]

    return li


li = [4,5,3,6,2,7,1,8,9]
print(len(li))

x = bubble_sort(li)
print(x)