'''
QUESTION:
438. Find All Anagrams in a String

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".



'''

from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        ans = []
        cnt_p = Counter(p)
        len_p = len(p)
        len_s = len(s)
        cnt_s = Counter(s[0:len_p])
        loop_index = len_s - len_p

        # for 0
        if cnt_s == cnt_p:
            ans.append(0)
        for index in range(len_s - len_p):
            cnt_s[s[index]] -= 1
            if cnt_s[s[index]] == 0:
                del cnt_s[s[index]]
            cnt_s[s[index + len_p]] += 1
            if cnt_s == cnt_p:
                ans.append(index + 1)
        return ans


'''
Idea/thoughts:
Going with creating counters for pattern and 
sliding window first part of the string, 
If the cnts are equal , add 0
then in range of string len - pattern len, check 

follow the process ,of : decrease cnt element by 1 
Little checking that , if cnt value of element becomes 0 remove it as that will create new cnt, which is overhead for the program exec

increment the index+len(p) counter by 1 .
and check if the cntrs are equal.
'''



