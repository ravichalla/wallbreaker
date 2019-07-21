

from math import floor
class Solution(object):
    def mid(self,left,right):
        return int(floor((right+left)/2))
    def peakIndexInMountainArray(self, A):
        left = 0
        right= len(A)-1
        pivot = self.mid(left,right)
        while( A[pivot-1]> A[pivot] or A[pivot]<A[pivot+1]):

            if A[pivot]>A[pivot+1]:
                right= pivot
                pivot = self.mid(left,right)
            else:
                left= pivot
                pivot = self.mid(left,right)
        return pivot
'''
Ideas/thoughts:
 using binary search, 

take a pivot as middle element, 
if the pivot'th element > pivot'th+1 element , then we can move the right pointer to pivot.
similarly ,in other case ,we can move the left pointer to pivot. 
calculate new mid value,with new left and right.
'''
