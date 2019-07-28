'''
QUESTION:
25. Reverse Nodes in k-Group

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        curr = head
        count = 0
        while count != k and curr:
            curr = curr.next
            count += 1
        if count == k:
            curr = self.reverseKGroup(curr, k)
            while count > 0:
                temp = head.next
                head.next = curr
                curr = head
                head = temp
                count -= 1
            head = curr
        return head


'''
Ideas/thoughts:
recursive approach of , 
take the head as current.
iterating thorough the elements , just making sure that the current is present and it donesn't reach count.

and again looping , placing tmp<- head next and head next <- curr and curr <- head and head <- tmp 
and finally head <- curr

'''