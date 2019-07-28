'''
QUESTION:

496. Next Greater Element I
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.

'''

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        res = []
        unordered_map = {}
        for i in nums2:
            while stack and i > stack[-1]:
                unordered_map[stack[-1]] = i
                stack.pop()
            stack.append(i)
        for j in nums1:
            if j in unordered_map:
                res.append(unordered_map[j])
            else:
                res.append(-1)
        return res


'''
Ideas/thoughts:
initialiting a map,stack and iterating thru nums2, 
checking if stack exists and no in nums2 > last element in stack ,  create a map with key as last ele of stack and value as no.
remove last element of stack and append no to stack.

and iterate thru nums1 , if no is present in map , append value to ans from map.
or else return -1 if not found.

'''