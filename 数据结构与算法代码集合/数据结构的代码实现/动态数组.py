class MyArrayList:
    # 设置初始容量为1
    INIT_CAP=1

    def __init__(self,init_capacity=None):
        self.data = [None] * (init_capacity if init_capacity is not None else MyArrayList.INIT_CAP)
        self.size=0
    
    
    # 程序将优先实现关键的API增删改查，
    # 而后写里面用到的功能性函数
    
    # 增
    def add_last(self, e):
        cap = len(self.data)
        # 看data数组容量够不够
        if self.size == cap:
            self._resize(2*cap)
        # 在尾部插入元素
        self.data[self.size] = e
        self.size +=1

    # 在任意索引位置添加元素
    def add(self,index,e):
        # 检查给的索引index是否正确，错误将抛出（raise）一个异常
        self._check_position_index(index)
        cap=len(self.data)
        if self.size == cap:
            self._resize(2*cap)
        
        #搬移数据 data[index] -> data[index+1]给新元素腾出位置
        for i in range(self.size-1, index-1, -1):
            self.data[i+1] = self.data[i]
        # 插入新元素
        self.data[index] = e
        self.size+=1
    def add_first(self,e):
        self.add(0,e)
    
    # 删
    def remove_last(self, e):
        if self.size == 0:
            raise Exception("Array is empty")
        cap = len(self.data)
        # 判断是否需要缩容
        if self.size <= cap//4:
            self._resize(cap//2)
        self.data[self.size - 1] = None
        self.size-=1
    def remove(self,index):
        # 检查索引是否越界
        self._check_element_index(index)
        cap = len(self.data)
        if self.size <= cap//4:
            self._resize(cap//2)
        #搬移数据
        for i in range(index, self.size-1):
            self.data[i] = self.data[i+1]
        self.data[self.size-1] = None
        self.size-=1
    def remove_first(self):
        return self.remove(0)
    # 查
    def get(self,index):
        # 检查索引越界
        self._check_element_index(index)
        return self.data[index]
    
    # 改
    def set(self, index, element):
        self._check_element_index(index)
        self.data[index]=element
    
    # 功能性方法

    # 扩容函数
    def _resize(self, new_cap):
        # 先新建一个大的空数组，再把原数组复制过来
        temp = [None] * new_cap
        for i in range(self.size):
            temp[i] = self.data[i]
        self.data = temp
    
    def _check_position_index(self,index):
        if not 0 <= index <= self.size:
            raise IndexError(f"Index: {index}, Size: {self.size}")
    def _check_element_index(self,index):
        if not 0 <= index < self.size:
            raise IndexError(f"Index: {index}, Size: {self.size}")

# 尝试创建实例化对象验证这个动态数组怎么样
if __name__ == "__main__":
    arr = MyArrayList(init_capacity=3)
    for i in range(1,6):
        arr.add_last(i)
    arr.remove(3)
    arr.add(1,9)
    
    print(arr.data)