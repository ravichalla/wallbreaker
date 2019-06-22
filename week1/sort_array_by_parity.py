'''
QUESTION:

Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.


Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
'''


class Solution(object):
    def sortArrayByParity(self, A):
        odd_lst = []
        even_lst = []
        for i in range(len(A)):
            if A[i] % 2 == 0:
                even_lst.append(A[i])
            else:
                odd_lst.append(A[i])

        return even_lst + odd_lst


'''
Idea/ thoughts:
   iterate through the array and find the even no.
   make array with odd no 
   make array with even no
   add odd + even
'''

