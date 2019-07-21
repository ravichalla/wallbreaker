
'''
QUESTION:
A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

'''

class Solution(object):
    def partitionLabels(self, S):

        last_indexs = {}
        start = 0
        end = 0
        result = []
        for index, char in enumerate(S):
            last_indexs[char] = index + 1

        for index, char in enumerate(S):
            end = max(end, last_indexs[char])
            if end == index + 1:
                length = end - start
                result.append(length)
                start = end
        return result


'''
Idea/thoughts:
find the last indexes of each character , by iterating thru the string and constructing a dict.
and iterate through it again ,  the end position would be , equal to max(end pos,element last pos).
if found the position, add the len upto there to ans.

'''