'''
QUESTION:
451. Sort Characters By Frequency
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
'''

from collections import Counter
class Solution:
    def frequencySort(self,s):
        c = Counter(str(s))
        ans=""
        for k, count in c.most_common():
            ans +="".join(k * count)
        return ans

'''
Ideas/thoughts:
create a counter for the list of string.
and most common will create descending order counter ,based on value
then concate to the ans string , times of count.
'''