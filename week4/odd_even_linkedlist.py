'''
QUESTION:

328. oddHead Even Linked List

Given a singly linked list, group all oddHead nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL


'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddHeadEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None or head.next.next is None:
            return head
        oddHead = head
        evenHead = head.next
        evenptr = head.next

        while evenHead.next and evenHead.next.next:
            oddHead.next = evenHead.next
            oddHead = oddHead.next

            evenHead.next = oddHead.next
            evenHead = evenHead.next

        if evenHead.next:
            oddHead.next = evenHead.next
            evenHead.next = None
            oddHead = oddHead.next
        oddHead.next = evenptr
        return head

'''
Ideas/thoughts: ( for putting oddHead , even nodes)
so, if the head is none or head next is none or just 2 elements in list ,then return head
iterating thourgh , until even next and even nextt next ele,
 connect oddHead to next oddHead and connect even to next even
if there is one more node then , connect to oddHead links,

time: o(n) , space : o(1) as we are using auxiliary variables.
'''