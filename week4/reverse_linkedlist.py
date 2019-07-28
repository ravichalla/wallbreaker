'''
QUESTION:
206. Reverse Linked List

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

'''

class Solution(object):
    def reverseList(self, head):
        curr = head
        if curr is None:
            return head
        if curr.next is None:
            return head
        p = self.reverseList(curr.next)
        curr.next.next = curr
        curr.next = None
        return p


'''
Ideas/thoughts:
1.check , if the curr is null then return,
2.if  curr .next is null.that means it is last node  and need to become the head and has to be the first node
3.recursively iterate thru list
4.set curr . next . next to curr
5.set curr .next to null 

'''