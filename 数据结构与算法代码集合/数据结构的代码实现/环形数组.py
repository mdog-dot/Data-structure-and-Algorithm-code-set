# 环形数组构建的关键在于取模%运算，通过维护start和end两个指针，
# 并且对于指针索引out of  index的情况进行取模运算，从而构造出一个环形数组
# 一般我们规定start和end的位置对应于一个左开右闭区间，即[start, end)
class CycleArray:
    def __init__(self, size=1):
        self.size = size
        self.arr = [None] * size
        # start指向第一个有效元素的索引，闭区间
        self.start = 0
        # end指向最后一个有效元素的下一个索引，开区间
        self.end = 0
        self.count = 0
    
    # 扩缩容函数
    def resize(self, newsize):
        # 扩容后的数组
        new_arr = [None] * newsize
        # 将元素复制到新数组
        # 注意在环形数组里面真正读取数组的时候应该是从start%self.size开始，
        # 不断+i直到取模后等于(end-1)%self.size
        for i in range(self.count):
            new_arr[i] = self.arr[(self.start+i)%self.size]
        self.arr = new_arr
        # 重置指针
        self.start = 0
        self.end = self.count
        self.size = newsize

    # 环形数组的优点在于可以以O（1）的时间复杂度在数组的头部增删元素
    # 原因是其通过对如索引位于-1的元素进行取模从而规避了对数组整体的移动

    # 在数组头部添加元素，O（1）
    def add_first(self, val):
        if self.is_full():
            self.resize(self.size * 2)
        self.start = (self.start-1) % self.size
        self.arr[self.start] = val
        self.count += 1
    
    # 删除数组头部元素，O（1）
    def remove_first(self):
        if self.is_empty():
            raise Exception("Array is empty")
        self.arr[self.start] = None
        self.start = (self.start + 1) % self.size
        self.count -= 1
        # 若数组元素过少，减小数组容量
        if self.count == self.size // 4:
            self.resize(self.size // 2)
    #在数组末尾添加元素，O（1）
    def add_last(self, val):
        if self.is_full():
            self.resize(self.size * 2)
        # end是开区间，先赋值会更方便
        self.arr[self.end] = val
        self.end = (self.end + 1) % self.size
        self.count += 1
    
    # 在数组末尾删除元素，O（1）
    def remove_last(self):
        if self.is_empty():
            raise Exception("Array is empty")
        self.end = (self.end-1) % self.size
        self.arr[self.end] = None
        self.count -= 1
        if self.count == self.size // 4:
            self.resize(self.size // 2)
        
    # 获取数组头部元素
    def get_first(self):
        if self.is_empty():
            raise Exception("Array is empty")
        return self.arr[self.start]
    # 获取尾部元素
    def get_last(self):
        if self.is_empty():
            raise Exception("Array is empty")
        return self.arr[(self.end -1) % self.size]
    
    # tool function
    def is_full(self):
        return self.count == self.size
    
    def is_empty(self):
        return self.count == 0
    
    