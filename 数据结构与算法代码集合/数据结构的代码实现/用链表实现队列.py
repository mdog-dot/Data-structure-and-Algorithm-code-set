# Python中的deque就是双链表
from collections import deque
class MyLinkedQueue:
    def __init__(self):
        self.list = deque()
    # 向队尾插入元素,O(1)
    def push(self, e):
        self.list.append(e)
    
    # 从队头删除元素，O(1)
    def pop(self):
        # 注意deque的popleft方法在删除元素时，还会返回删除掉的元素
        return self.list.popleft()
    
    # 查看队头元素，O(1)
    def peek(self):
        return self.list[0]

    # 返回队列中元素个数，O(1)
    def size(self):
        return len(self.list)
        