# 拉链法的核心就是当遇到不同的key在hash函数中映射到相同index值的情况（哈希冲突），
# 通过将底层数组table每一个索引位置的元素设置成一个链表，链表中存放
# hash到相同index的不同key-value对，该链表也可以用简单的数组实现

# 关于哈希表的实现还有其他几个麻烦
# 1.构造合适的hash函数将各种类型的key（string or int）映射为正整数型的index
# 2.当哈希表中底层数组大小偏小或哈希表中存储的元素数量过多时，其负载因子过大，
# 导致哈希冲突发生的概率较高，故一般设定当负载因子达到默认值时会动态扩缩容

class KVNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class MyChainingHashMap:
    def __init__(self, capacity = 1):
        self.size = 0
        self.capacity = capacity
        # 初始化底层数组table
        self.table = [[] for _ in range(self.capacity)]

    # _hash函数用来将key映射到数组内的某个index索引，hash函数是Python中的内置函数，可以返回任意可哈希变量的哈希值

    def _hash(self, key):
        return hash(key) % self.capacity
        
    # 增/改  如果key不存在，添加key-value对；如果不存在，则将key对应的value修改
    def put(self, key, value):
        index = self._hash(key)
        _list = self.table[index]
        for node in _list:
            if node.key == key:
                node.value = value
                return
        _list.append(KVNode(key, value))
        self.size += 1
        # 如果元素数量超过了负载因子，则对table进行扩容
        if self.size >= self.capacity * 0.75:
            self._resize(self.capacity * 2)
    
    # 删   删除key和对应的value
    def remove(self, key):
        index = self._hash(key)
        _list = self.table[index]
        for node in _list:
            if node.key == key:
                _list.remove(node)
                self.size -= 1

                #缩容，当负载因子小于0.125时，减小table容量
                if self.size <= self.capacity // 8:
                    self._resize(max(self.capacity //4 , 1))

    # 查  如果key存在，返回value；如果不存在，返回None
    def get(self, key):
        index = self._hash(key)
        _list = self.table[index]
        for node in _list:
            if node.key == key:
                return node.value
        return None

    # 返回所有keys
    def keys(self):
        keys = []
        for item in self.table:
            for node in item:
                keys.append(node.key)
        return keys

    # tool function
    # 扩容函数
    def _resize(self, new_capacity):
        # 在方法中是可以实例化对象的，因为方法是等到被调用时才执行，除非在该方法里实例化对象之后
        # 再次调用该方法，这样才会造成递归出错
        new_table = MyChainingHashMap(new_capacity)
        for item in self.table:
            for node in item:
                new_table.put(node.key, node.value)
        # 个人认为直接复制数组也不是不可以，只是会导致key所对应的index不再符合由hash函数计算出来的索引
        self.table = new_table.table
        self.capacity = new_capacity
    
if __name__ == "__main__":
    map = MyChainingHashMap()
    map.put(1, 1)
    map.put(2, 2)
    map.put(3, 3)
    print(map.get(1))  # 1
    print(map.get(2))  # 2