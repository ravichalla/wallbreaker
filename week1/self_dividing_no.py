'''
QUESTION:

728. Self Dividing Numbers
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:
Input:
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

'''


class Solution(object):
    def cal_fn(self, no):
        digit_lst = [int(d) for d in str(no)]
        if 0 in digit_lst:
            return False
        for digit in digit_lst:
            if no % digit != 0:
                return False
        return True

    def selfDividingNumbers(self, left, right):
        ans = []
        for no in range(left, right + 1, 1):
            if self.cal_fn(no) == True:
                ans.append(no)
        return ans


'''
iterate through range of no,
write a fn, which tells true if it is self diving 
return a  ans list ,with those no, for  which that fn. returns true
'''