'''

QUESTION:
232. Implement Queue using Stacks

'''


class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.stack2) != 0:
            tmp = self.stack2.pop()
        else:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())
            tmp = self.stack2.pop()
        return tmp

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.stack2) != 0:
            return self.stack2[-1]
        else:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())
            return self.stack2[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

'''
Ideas/thoughts:
for implementing the queue using stacks ,

first initilaize 2 stacks empty. then for push , append ele to stack 1

for popping, check if stack2 is not empty, then pop last element to return , if found stack2 as empty, then stack popping ele from stack1 and append to stack2 . 
then return last ele as removed ele

for peeking , which gives ele of front of queue, not by removing it . if stack2 is not empty, then return last ele of stack2, otherwise , continuously pop elements in stck1 and add in stack2 and finally return last ele of stack2 , which will be first ele of queue.


empty check function is , if both stack2 are zero , then empty otherwise not.

'''