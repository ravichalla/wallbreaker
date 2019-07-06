'''
QUESTION:
205. Isomorphic Strings
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true


'''

class Solution(object):
    def isIsomorphic(self, s, t):
        iso_dict = dict()

        for S, T in zip(s, t):
            if S not in iso_dict:
                iso_dict[S] = T
            elif iso_dict[S] != T:
                return False
        return len(set(iso_dict.values())) == len(iso_dict.values())


'''
Ideas/thoughts:
create a single dict,
it contains the keys from s and values from t.

only one char in s can map to one char in t.
As keys wouldn't be duplicate, we can get track if any other char in s have diff mapping in t.
then return false.
there is , where two diff keys map to same value, which is not possible.
'''