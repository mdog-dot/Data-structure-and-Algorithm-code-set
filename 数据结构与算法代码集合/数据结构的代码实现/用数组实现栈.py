class MyArrayStack:
    def __init__(self):
        self.list = []
    # 向栈顶加入元素，O(1)
    def push(self, e):
        self.list.append(e)
    
    # 从栈顶弹出元素，O(1)
    def pop(self):
        self.list.pop()
    
    # 查看栈顶元素，O（1）
    def peek(self):
        return self.list[-1]
    
    # 返回栈中元素个数，O(1)
    def size(self):
        return len(self.list)
    