def select_sort(li):
    for i in range(len(li)-1):
        min = i
        for j in range(i+1, len(li)):
            if li[j] < li[min]:
                li[j], li[min] = li[min], li[j]

    return li

li = [3,2,4,7,6,5,1,9,8]

print(select_sort(li))