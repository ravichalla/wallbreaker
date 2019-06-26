'''
QUESTION:

868. Binary Gap
Given a positive integer N, find and return the longest distance between two consecutive 1's in the binary representation of N.

If there aren't two consecutive 1's, return 0.



Example 1:

Input: 22
Output: 2
Explanation:
22 in binary is 0b10110.
In the binary representation of 22, there are three ones, and two consecutive pairs of 1's.
The first consecutive pair of 1's have distance 2.
The second consecutive pair of 1's have distance 1.
The answer is the largest of these two distances, which is 2.
Example 2:

Input: 5
Output: 2
Explanation:
5 in binary is 0b101.
Example 3:

Input: 6
Output: 1
Explanation:
6 in binary is 0b110.
Example 4:

Input: 8
Output: 0
Explanation:
8 in binary is 0b1000.
There aren't any consecutive pairs of 1's in the binary representation of 8, so we return 0.


'''


class Solution(object):
    def binaryGap(self, N):
        index_lst = []
        b = bin(N)[2:]
        for i in range(len(b)):
            if b[i] == '1':
                index_lst.append(i)
        max = 0
        for i in range(len(index_lst) - 1):
            if (index_lst[i + 1] - index_lst[i]) > max:
                max = index_lst[i + 1] - index_lst[i]
        return max


'''
Ideas/thoughts:
convert the binary and find the positions of 1's and 
and see the long diff of digits.

'''

