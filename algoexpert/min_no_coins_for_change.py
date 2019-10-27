'''
Given an array of positive integers representing coin denominations and a single non-negative integer representing
 a target amount of money, implement a function that returns the smallest number of coins needed to make change for that target amount using the given coin denominations. Note that an unlimited amount of coins is at your disposal.
If it is impossible to make change for the target amount, return -1.



6 [1,2,4]
output 2   [ 2+4 ]

'''



def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
    nums = [float("inf") for _ in range(n+1)]
	nums[0]=0
	for denom in denoms:
		for amnt in range(n+1):
			if denom <= amnt:
				nums[amnt]= min(nums[amnt], 1+nums[amnt-denom])
	return nums[n] if nums[n]!= float("inf") else -1