class Queue:
    def __init__(self,size = 100):  # 构造函数
        self.queue = [0 for _ in range(size)]  # 创建队列，固定长度100
        self.size = size
        self.front = 0 #  队列开头
        self.rear = 0  # 队列结尾

    def push(self, element):
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = element

    def pop(self):
        self.front = (self.front + 1) % self.size
        return self.queue[self.front]

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return (self.rear + 1) % self.size == self.front


