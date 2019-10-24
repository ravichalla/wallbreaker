# imple. using arr - queue
class q:

    def __init__(self):
        self._capacity = 5
        self._n =0 # track cap
        self._arr = [None] * self._capacity

    def isEmpty(self):
        if self._n ==0 :
            return True
        else:
            return False

    def size(self):
        return self._n

    def pushback(self, key):
        self._arr[self._n ]== key
        if self._n== self._capacity-1:
            b = [None] * 2 * self._capacity
            for i in range(self._n):
                b[i]== self._arr[i]
            b[self._n] = key
            self._arr = b
        else:
            self._arr[self._n]= key
        self._n +=1

    def popFront(self,key):



