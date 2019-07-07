class MyHashSet:
    def __init__(self):
        self.capacity = 5000
        self.arr = [None] * self.capacity

    def add(self, key):
        hash_val = hash(key) % self.capacity
        if self.arr[hash_val] == None:
            self.arr[hash_val] = [key]
        else:
            if key not in self.arr[hash_val]:
                self.arr[hash_val].append(key)

    def remove(self, key) -> None:
        hash_val = hash(key) % self.capacity
        if self.arr[hash_val] == None:
            return
        for ind in range(len(self.arr[hash_val])):
            if self.arr[hash_val][ind] == key:
                del self.arr[hash_val][ind]
                return

    def contains(self, key):
        hash_val = hash(key) % self.capacity
        if self.arr[hash_val] == None:
            return False
        else:
            for h_key in self.arr[hash_val]:
                if h_key == key:
                    return True
            return False
