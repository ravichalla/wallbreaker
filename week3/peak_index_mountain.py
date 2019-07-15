def peakIndexInMountainArray( A):
    left = 0
    right = len(A) - 1

    while left <right:
        mid = (left+right)/2
        if A[left]<A[right]:
            mid= left+1


print(peakIndexInMountainArray([0,2,1,0]))

'''
Ideas/thoughts:
peak is something, to the left all values are small and for right also all values small.
when ascending the mountina, the next value will be higher than bfr value.
'''