'''
QUESTION:

290. Word Pattern
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
'''

class Solution(object):
    def wordPattern(self, pattern, str):
        s = [x for x in pattern]
        t = str.split(" ")
        # sanity check of len
        if len(s) != len(t):
            return False
        word_map = dict()
        for S, T in zip(s, t):
            if S not in word_map:
                word_map[S] = T
            elif word_map[S] != T:
                return False
        return len(set(word_map.values())) == len(word_map.values())


'''
Ideas/thoughts:
convert the strings to list and do a sanity check if lens are equal. if not return false
if lists len are equal , make a dict, with conditions if element not present add it.
if element present, it should not be mapped to diff value.
the values should be equal too, abbe - dddd
'''