def b_search(li,val):
    l = 0
    r = len(li) - 1
    while l <= r:
        m = (l + r) // 2
        if li[m] == val:
            return m

        elif li[m] > val:
            r = m - 1

        else:
            l = m + 1

    else:
        return None


li = [1,2,3,4,5,6,7,8]
val = 1

x = b_search(li,val)

print(x)



