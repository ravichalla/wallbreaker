'''
QUESTION:
856. Score of Parentheses
Given a balanced parentheses string S, compute the score of the string based on the following rule:

() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.

Example 1:

Input: "()"
Output: 1
Example 2:

Input: "(())"
Output: 2
Example 3:

Input: "()()"
Output: 2
Example 4:

Input: "(()(()))"
Output: 6


'''
class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = [0]
        for c in S:
            if c == "(":
                stack.append(0)
            else:
                last = stack.pop()
                stack[-1] += (2 * last) or 1
        return stack.pop()


'''
Ideas/thoughts:
create a stack with value as 0 , 
and char ( found, append 0, 
if not found, add to the last stack ele twice last stack ele or 1  ,which one is bigger, 

finally answer woudl be result of the stack last ele, cause adding the count to it.

'''