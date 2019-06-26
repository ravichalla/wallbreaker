'''
QUESTION:
171. Excel Sheet Column Number
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701

'''
class Solution(object):
    def titleToNumber(self, s):
        ans = 0
        l = len(s)
        for c in s:
            ans += (26 ** (l - 1)) * (ord(c) - 64)
            l = l - 1
        return ans


'''
Ideas/thoughts:
for each char in string,
multiply with 26*power to which it has to raise and  multiply with the ord-64 which is 
the exact char no
sum all values 

'''        

print("a".isalnum())

