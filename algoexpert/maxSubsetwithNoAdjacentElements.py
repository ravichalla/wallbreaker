'''
Write a function that takes in an array of positive integers and returns an integer representing the maximum sum of non-adjacent elements
in the array.
If a sum cannot be generated, the function should return 0.

[7,10,12,7,9,14] 7+12+14=33
'''


# O(n) time | O(n) space
# def maxSubsetSumNoAdjacent(array):
#     # Write your code here.
# 	if not len(array):
# 		return 0
# 	elif len(array)==1:
# 		return array[0]
# 	maxSums = array[:]
# 	maxSums[1] = max(array[0], array[1])
# 	for i in range(2, len(array)):
# 		maxSums[i] = max(maxSums[i-1], maxSums[i-2]+ array[i])
# 	return maxSums[-1]

def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return 0
    elif len(array) == 1:
        return array[0]
    second = array[0]
    first = max(array[0], array[1])
    for i in range(2, len(array)):
        current = max(first, second + array[i])
        second = first
        first = current
    return first
