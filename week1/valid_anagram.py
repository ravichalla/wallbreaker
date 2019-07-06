'''
QUESTION:
242. Valid Anagram
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?


'''


class Solution(object):
    def isAnagram(self, s, t):
        # sanity check
        if len(s) != len(t):
            return False
        dic = dict()

        for char in s:
            dic[char] = dic.get(char, 0) + 1
        for char in t:
            dic[char] = dic.get(char, 0) - 1

        for char in t:
            if dic[char] != 0:
                return False
        return True


'''
Ideas/thoughts:
I want to use dictionary and count the no of each char , 
for 1 list , use count ++ for each for 2nd list, decrease count --, in that way no need to 
take two dicts.
and check count 

'''