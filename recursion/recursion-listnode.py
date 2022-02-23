class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1: return l2  # 终止条件，直到两个链表都空
        if not l2: return l1
        if l1.val <= l2.val:  # 递归调用
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2

class ListNode(object):
    def __init__(self, val = 0, next = None):
        self.val = val  # 数据域
        self.next = next  # 指针域

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)

n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)

n1.next = n3
n3.next = n5

n2.next = n4
n4.next = n6


r = []

solution = Solution().mergeTwoLists(n1, n2)

# print(solution.next.next.val)

while solution:
    r.append(solution.val)
    solution = solution.next

print(r)