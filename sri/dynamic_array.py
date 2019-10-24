class Vector:
    def __init__(self):
        self._n =0
        self._capacity = 4
        self._a = [None] * self._capacity

    def size(self):
        return self._n

    def isEmpty(self):
        if self._n==0:
            return True
        return False
    # returns item at given index, blows up if index out of bounds
    def at(self, index):
        if index < 0 or index >= self._capacity:
            print("Index out of bounds")
        return self._a[index]

    def re_size(self,c):
        b = [None]* c
        for i in range(len(self._a)):
            b[i]= self._a
        self._a= b

    def resize(self, c):
        b = [None] * c
        for i in range(len(self._a)):
            b[i] = self._a[i]
        self._a = b
        self._capacity =c


    # push back
    def push_back(self,item):
        if self._n == self._capacity:
            self.resize(2 * self._capacity)
        self._a[self._n] = item
        self._n += 1
        return self._a

    def insert(self, index, item):
        if index < 0 :
            print("Error")
        if self._n == self._capacity:
            self.resize(2 * self._capacity)
        for i in range((len(self._a) - 1), index, -1):
            self._a[i] = self._a[i - 1]
        self._a[index] = item
        self._n += 1
        return self._a

    # remove from end, return value
    def pop(self):
        temp = self._a[self._n -1]
        self._a[self._n - 1]=None
        self._n -=1
        return temp

    def delete(self,index):
        if index<0 or index>= self._n:
            print("index not there")
            return
        for i in range(index,self._n,+1):
            self._a[i]=self._a[i+1]
            self._a[self._n-1]=None
        self._n-=1
        return self._a


    def re_move(self,item):
        for i in range(len(self._a)):
            if self._a[i]== item:
                self._a[i] == None
                if self._n == self._capacity:
                    self._a[self._n -1] == None
                    break
                for j in range(i,self._n, +1):
                    self._a[j] = self._a[j+1]
        self._n -= 1
        return  self._a

    def remove(self, item):
        for i in range(len(self._a)):
            if self._a[i] == item:
                self._a[i] == None
                if self._n == self._capacity:
                    self._a[self._n - 1] == None
                    break
                for j in range(i, self._n, +1):
                    self._a[j] = self._a[j + 1]

        self._n -= 1
        return self._a



    def find(self,item):
        for i in range(len(self._a)):
            if self._a[i]== item:
                return i



def main():
    v = Vector()
    print(v.size())
    print(v.isEmpty())
    print(v.push_back(3))
    print(v.push_back(5))
    print(v.push_back(6))
    print(v.push_back(32))
    print(v.push_back(22))
    print(v.push_back(22))
    print(v.insert(2,8))
    #print(v.insert(8,8))
    print(v.size())
    print(v.delete(2))
    print(v.remove(6))

if __name__ == "__main__":
    main()