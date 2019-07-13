'''
QUESTION:
392. Is Subsequence
Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.

'''



class Solution(object):
    def isSubsequence(self, s, t):
        s_pointer = 0
        t_pointer = 0
        len_s = len(s)
        len_t = len(t)
        while s_pointer < len_s and t_pointer < len_t:
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
                if s_pointer == len_s:
                    break
                t_pointer += 1
            else:
                t_pointer+=1
        return s_pointer == len_s


'''
Ideas/thoughts:
while the len of strings are there.
check if the first char matches in s matches , char in t. incrment the s pointer , but bfr incremetning the t pointer, check if s reached max len, 
if not return index and len(s) compare condition.

'''
