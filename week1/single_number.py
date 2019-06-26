'''
QUESTION:
136. Single Number

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4

'''
class Solution(object):
    def singleNumber(self, nums):
        return reduce(lambda x, y: x ^ y, nums)

'''
Ideas/thoughts:
This can be achieved by xor .
Reduce fn takes a fn and a iterator.
lambda fn, can take any params ,but one exp. that is xor can be given.

'''