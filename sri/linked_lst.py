class Node:
    def __init__(self, key, next=None):
        self.key = key
        self.next = next


class Sll:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.n = 0

    def size(self):
        return self.n

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    def value_at(self, index):
        current = self.head
        if current is None:
            return None
        elif index < 0 or index >= self.n:
            print("invalid index")
        else:
            i = 0
            while i != index:
                current = current.next
                i += 1
            return current.key

    def push_front(self, key):
        node = Node(key)
        node.next = self.head
        self.head = node
        if self.tail == None:
            self.tail = node
        self.n += 1

    def display(self):
        current = self.head
        while current is not None:
            print(current.key, end="->")
            current = current.next
        return

    def insert(self, i, val):
        if i == 0:
            node = Node(val)
            node.next = self.head
            self.head = node
        elif i == self.n - 1:
            node = Node(val)
            node.next = None
            self.tail.next = node
            self.tail = node
        elif i < 0 or i >= self.n:
            return False
        else:
            p = self.head
            j = 0
            while j + 1 != i:
                p = p.next
                j += 1
            node = Node(val)
            node.next = p.next
            p.next = node
        self.n += 1

    def erase(self,index):




def main():
    sll=Sll()
    print(sll.insert(0,4))
    print(sll.insert(1,5))
    print(sll.insert(2,6))
    print(sll.insert(3,7))


if __name__=="__main__":
    main()