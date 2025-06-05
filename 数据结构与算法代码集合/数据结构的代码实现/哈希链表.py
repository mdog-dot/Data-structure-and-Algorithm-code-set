# 一般的哈希表由于对底层数组扩缩容时会改变key在哈希函数中对应的index值，因此key的顺序是乱序的，
# 不能依赖key的顺序进行编程（如遍历），但是假如我们把哈希表与双链表结合起来，即每个键值对对应一个节点
# 然后用一个双链表把这些节点串起来，key指向对应节点，于是增删改查认为O(1)，且key按顺序排列在链表中，
# 这就是哈希链表，在Python语言中对应于字典dict

# 注意：所谓拉链法和开放寻址法，只是介绍一下哈希表底层的实现逻辑，真正考虑哈希表时，
# 只需要把他当作一个键和值的映射即可

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
class MyLinkedHashMap:
    def __init__(self):
        # 构建双链表
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        # 构建哈希表（哈希映射），这里使用Python自带的哈希链表dict，但是不使用其顺序性，
        # 只使用其作为哈希表的性质，因此也可以换成任意一个之前已经构建好的哈希表
        # self.map的作用是存下key对应于双链表中的节点位置(一般哈希表是把key映射到数组index位置的元素，这里是把key映射到双链表的节点)
        self.map = dict()
    
    def put(self, key, val):
        if key not in self.map:
            node = Node(key, val)
            self.map[key] = node
            self.add_last_node(node)
            return
        self.map[key].val = val
    
    def remove(self, key):
        if key not in self.map:
            return
        node = self.map[key]
        self.remove_node(node)
        del self.map[key]
    
    def add_last_node(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
    
    def remove_node(node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None
    
    def get(self, key):
        if key not in self.map:
            return None
        return self.map[key].val
    
    def keys(self):
        key_list = []
        # 这里我们只把self.map当成一个一般的哈希表，因此其中的key的顺序是乱序的，故不能遍历self.map获得key
        # 要按顺序输出所有key，应该遍历链表
        p = self.head.next
        while p != self.tail:
            key_list.append(p.key)
            p = p.next
        return key_list
    

    
        