#l = [-1,0,1,2,-1,-4]

l = [1,1,1,1]
target = 0

l.sort()

print(l)
print(len(l))

res = []

for i in range(len(l)):
    #print(i)

    l_p = i + 1
    r_p = len(l) - 1

    while l_p < r_p:
        if l[i] > 0:
            break
        if l[i] + l[l_p] + l[r_p] == 0:
            res.append([l[i], l[l_p], l[r_p]])
            break
        elif l[i] + l[l_p] + l[r_p] < 0:
            l_p += 1
        else:
            r_p -= 1


print(res)



