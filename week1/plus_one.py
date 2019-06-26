'''

QUESTION:
66. Plus One
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

'''

class Solution(object):
    def plusOne(self, digits):
        str_lst = [str(digit) for digit in digits]
        no = int("".join(str_lst))
        no = no + 1
        ans = [int(digit) for digit in str(no)]
        return ans


'''
Ideas/thoughts:
convert the given int lst to str list and use join which takes iterable list to make str
then type cast to int
add +1 to no
and make the int list from a iterable str.

'''