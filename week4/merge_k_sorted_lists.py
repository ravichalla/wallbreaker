<<<<<<< HEAD
'''
QUESTION:
23. Merge k Sorted Lists

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6


'''


=======
>>>>>>> files added
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

<<<<<<< HEAD
import heapq
=======
from Queue import PriorityQueue


>>>>>>> files added
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
<<<<<<< HEAD
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heap.append((lists[i].val,lists[i]))
        heapq.heapify(heap)
        
        dummy = ListNode(None)
        cur = dummy
        while heap:
            num,node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(heap,(node.next.val,node.next)) 
        return dummy.next
    
'''
Ideas/thoughts:
Initialize a heap , and iterate thorugh the lists , 
append tuple with values lists val , lists . 
and finally heapify after appending.

creating a dummy listnode and a pointer , iterate through heap , 
If the next to node is there, heap push val,node.next

and finally return the var next , as here dummy.
'''
=======
        head = point = ListNode(0)
        q = PriorityQueue()
        for lst in lists:
            if lst:
                q.put((lst.val, lst))
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next


'''
Ideas/thoughts:
initiliaze result and heap . 

'''








>>>>>>> files added
