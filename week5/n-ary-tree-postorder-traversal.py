"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
'''
# recursive sol.
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans=[]
        if root == None: return ans
        def recursion(root,ans):
            for child in root.children:
                recursion(child,ans)
            ans.append(root.val)
        recursion(root,ans)
        return ans
'''

#iterative sol
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans =[]
        if root == None: return ans
        stack = [root]
        while stack:
            curr = stack.pop()
            ans.append(curr.val)
            stack.extend(curr.children)
        return ans[::-1]


'''
Ideas/thoughts:
# recursive sol
the common sol is recursion, if root empty return empty
else recursively call ( root, ans(ans will be res of res append of root) )


#iterative sol
# wkt ques is postorder, for going iterative, 
we can think, -- iteration is basically preorder traversal ,but rather going left,right ,reverse the result. 

If root is None , return empty ,
else , take stack root element as curr and append to ans
using stack extending(add each ele to stack, instead of direct list) with children of root.
return reversed list
'''