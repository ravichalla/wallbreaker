''''
QUESTION:
20. Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack =[]
        dict= { "]": "[" , "}": "{" , ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack==[] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []

'''
Ideas/thoughts:
initialize a stack and create a dict with } , ] , ( as keys
iterate thru list , if char is present in dict values,
if present , then append to stack.

if not in values, check if it the stack is empty (that means for first char encontered) OR dict value not equal to last ele of stack, return false
in any other case also return false.

finally return , the check if stack is empty , which should be in our case.

'''