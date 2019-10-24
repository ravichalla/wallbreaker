# PYTHON 3 IN LEETCODE EDITOR

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.iterative(root1,[]) == self.iterative(root2,[])
    def iterative(self,root,s):
        if root is not None:
            stack=[]
            stack.append(root)
            while stack:
                x = stack.pop(-1)
                if x.left is None and x.right is None:
                    s.append(x.val)
                    continue
                if x.right is not None:
                    stack.append(x.right)
                if x.left is not None:
                    stack.append(x.left)
        return s

'''
Ideas/thoughts:
call a fn. iterative which contains , 
check if root is not empty  and then make add root to stack and add to stack from left or right, if not present.

'''