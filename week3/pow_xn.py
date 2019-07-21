'''
QUESTION:
50. Pow(x, n)
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

'''

class Solution(object):
    def myPow(self, x, n):
        if n < 0:
            n = -n
            x = (1 / x)
        if n == 0:
            return 1
        elif n % 2 == 0:
            y = self.myPow(x, n / 2)
            return y * y
        else:
            return x * self.myPow(x, n - 1)


'''
Ideas/thoughts:

Using recursion and memoization technique,
If the even power , like 4 there , no need to calculate mypow twice , just call once and save in y.

'''