# 节点定义：
class Node(object):


    def __init__(self, item):
        self.item = item  # 数据域
        self.next = None  # 指针域


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

n1.next = n2
n2.next = n3

print(n1.item)
# 通过 n1 找到n3的值
print(n1.next.next.item)