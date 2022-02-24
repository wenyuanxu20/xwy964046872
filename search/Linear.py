# coding = utf-8
# O(n) Linear Search

def Linear_search(li, val):
    for ind, v in enumerate(li):
        if v == val:
            return ind
        else:
            return None


li = [1,2,3]

val = 1

x = Linear_search(li, val)

print(x)