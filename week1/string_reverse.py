'''
QUESTION:

344. Reverse String
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.


Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]


'''

class Solution(object):
    def reverseString(self, s):
        leftindex = 0
        rightindex = len(s) - 1
        while (leftindex < rightindex):
            s[leftindex], s[rightindex] = s[rightindex], s[leftindex]
            leftindex += 1
            rightindex -= 1


'''
Ideas/thoughts:
As need to modify in place, without creating new array.
As python can do pair value assign,
assign left to right, right value to left until leftindex is less than right.

No need to return anything

'''