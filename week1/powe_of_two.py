'''
QUESTION:
231. Power of Two

Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true
Explanation: 20 = 1
Example 2:

Input: 16
Output: true
Explanation: 24 = 16
Example 3:

Input: 218
Output: false

'''

class Solution(object):
    def isPowerOfTwo(self, n):
        i = 1
        while (i < n):
            i = i * 2

        return (i == n)


'''
Ideas/thoughts:

1, 2, 8, 16, 32, 64 
initialize with 1 , 
checking if the var is less than given, 
multiply var by 2 until var is less than given.

return true based on the given value and var is equal

'''