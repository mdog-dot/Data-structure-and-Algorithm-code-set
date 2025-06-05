class Node:
    def __init__(self,val):
        self.val=val
        self.next = None
        self.prev = None
class MyLinkedList:
    # 虚拟头尾节点
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    # 增
    def add_last(self, e):
        x = Node(e)
        self.tail.prev.next = x
        x.next = self.tail
        x.prev = self.tail.prev
        self.tail.prev = x
        self.size += 1
    
    def add_first(self, e):
        x = Node(e)
        self.head.next.prev = x
        x.next = self.head.next
        x.prev = self.head
        self.head.next = x
        self.size += 1
    
    def add(self, index, e):
        self._check_position_index(index)
        if index == self.size:
            self.add_last(self, e)
            return
        # 找到index位置对应的节点
        p = self.get_node(index)
        x = Node(e)
        p.prev.next = x
        x.prev = p.prev
        x.next = p
        p.prev = x
        self.size += 1

    # 删
    def remove_first(self):
        if self.size<1:
            raise IndexError("No elements to remove")
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next
        self.size-=1
    
    def remove_last(self):
        if self.size<1:
            raise IndexError("No elements to remove")
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev
        self.size-=1

    def remove(self, index):
        self._check_element_index(index)
        # 找到index位置对应的Node
        x = self.get_node(index)
        x.prev.next = x.next
        x.next.prev = x.prev
        self.size -= 1
    
    # 查
    def get_node(self, index):
        self._check_element_index(index)
        p = self.head
        for _ in range(index+1):
            p = p.next
        return p
    
    def get(self, index):
        self._check_element_index(index)
        p = self.get_node(index)
        return p.val
    
    # 改

    def set(self, index, val):
        self._check_element_index(index)
        p = self.get_node(index)
        p.val = val
    
    # tool function
    def _check_element_index(self, index):
        if not 0 <= index <= self.size-1:
            raise IndexError(f"Index: {index}, Size: {self.size}")
    
    def _check_position_index(self, index):
        if not 0 <= index <= self.size:
            raise IndexError(f"Index: {index}, Size: {self.size}")
    
    #可视化工具函数、
    def display(self):
        print(f"size = {self.size}")
        p = self.head.next
        while p != self.tail:
            print(f"{p.val} <->", end=" ")
            p = p.next
        print("null\n")
    

    # 实验
if __name__ == "__main__":
    list = MyLinkedList()
    list.add_last(1)
    list.add_last(2)
    list.add_last(3)
    list.add_first(0)
    list.add(2, 100)

    list.display()