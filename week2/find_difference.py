'''
QUESTION:
389. Find the Difference

Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

Example:

Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.

'''

from collections import Counter
class Solution:
    def findTheDifference(self, s, t):
        return "".join( (Counter(t) - Counter(s)).keys() )

'''
Ideas/thoughts:
return string of counters diff keys.

'''