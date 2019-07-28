'''
QUESTION:
146. LRU Cache

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

'''

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoubleLL(object):
    def __init__(self):
        self.dummy = ListNode(0)
        self.tail = self.dummy
        self.size = 0

    def add_to_head(self, node):
        self.dummy.next, node.next, node.prev = node, self.dummy.next, self.dummy
        if node.next:
            node.next.prev = node
        if self.tail is self.dummy:
            self.tail = self.tail.next
        self.size += 1

    def del_node(self, node):
        if not node:
            return
        if node is self.tail:
            self.tail = self.tail.prev
        node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        self.size -= 1


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.queue, self.dic, self.size, self.n = DoubleLL(), {}, capacity, 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dic:
            node = self.dic[key]
            self.queue.del_node(node)
            self.queue.add_to_head(node)
            return node.val[1]
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.dic and self.queue.size >= self.size:
            rem_node = self.queue.tail
            self.queue.del_node(rem_node)
            self.dic.pop(rem_node.val[0], None)

        self.queue.del_node(self.dic.pop(key, None))
        self.queue.add_to_head(ListNode((key, value)))
        self.dic[key] = self.queue.dummy.next


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

'''
Ideas/thoughts:
implement a NodeList and Double Linked List(with add nodes, del node)
implement the put ,get accordingly.

'''