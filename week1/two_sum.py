'''
QUESTION:
1. Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''


class Solution(object):
    def twoSum(self, nums, target):
        complement_dict = dict()
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if num in complement_dict:
                return [complement_dict[num], i]
            else:
                complement_dict[complement] = i


'''
Ideas/thoughts:

To make it optimized , instead of going with two for-loops and finding the second no.

Going with creation of dict,dict contains key as complement no and value as index of complement_no.
iterate the range. 

'''
