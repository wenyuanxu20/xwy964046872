from collections import deque  # 双向队列

q = deque([9,8,7],3)
q.append(1)
q.append(2)
q.appendleft(3)
print(q)

q.popleft()  # 从左边pop
q.pop() # 从右边pop

print(q)

