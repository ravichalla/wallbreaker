class MyHashMap:
    def __init__(self):
        self.cap = 5000
        self.arr = [None] * self.cap

    def put(self, key, value):
        hash_val = hash(key) % self.cap
        if self.arr[hash_val] == None:
            self.arr[hash_val] = [(key, value)]
        else:
            for ind in range(len(self.arr[hash_val])):
                tup = self.arr[hash_val][ind]
                if tup[0] == key:
                    self.arr[hash_val][ind] = (key, value)
                    return
            self.arr[hash_val].append((key, value))

    def get(self, key):
        hash_val = hash(key) % self.cap
        if self.arr[hash_val] != None:
            for tup in self.arr[hash_val]:
                if tup[0] == key:
                    return tup[1]
        return -1

    def remove(self, key):
        hash_val = hash(key) % self.cap
        if self.arr[hash_val] != None:
            for ind in range(len(self.arr[hash_val])):
                if self.arr[hash_val][ind][0] == key:
                    del self.arr[hash_val][ind]
                    return

'''
Idea/thoughts:
implement the put, get , remove mehtods,
used a hash and list of size 5000, it can be any no.

put each ele in hash position.
'''