'''
QUESTION:
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

'''


class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        min_index = min([len(str) for str in strs])
        succ_cnt = 0
        value = strs[0][:min_index]
        while (succ_cnt != len(strs) and min_index > 0):
            succ_cnt = 0
            for lst_index, stri in enumerate(strs):
                if stri[:min_index] == value[:min_index]:
                    succ_cnt += 1
                    continue
                else:
                    min_index -= 1
        return value[:min_index]


'''
Ideas/thoughts:

Need to consider, if the empty input is sent, return ""
else do the ,
iterate thru list and check min len of str and
check starting with the min len index of str , if strs have same 

decrease it if not

return ,the final lst.

'''