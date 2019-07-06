'''
QUESTION:
893. Groups of Special-Equivalent Strings
You are given an array A of strings.

Two strings S and T are special-equivalent if after any number of moves, S == T.

A move consists of choosing two indices i and j with i % 2 == j % 2, and swapping S[i] with S[j].

Now, a group of special-equivalent strings from A is a non-empty subset S of A such that any string not in S is not special-equivalent with any string in S.

Return the number of groups of special-equivalent strings from A.



Example 1:

Input: ["a","b","c","a","c","c"]
Output: 3
Explanation: 3 groups ["a","a"], ["b"], ["c","c","c"]
Example 2:

Input: ["aa","bb","ab","ba"]
Output: 4
Explanation: 4 groups ["aa"], ["bb"], ["ab"], ["ba"]
Example 3:

Input: ["abc","acb","bac","bca","cab","cba"]
Output: 3
Explanation: 3 groups ["abc","cba"], ["acb","bca"], ["bac","cab"]
Example 4:

Input: ["abcd","cdab","adcb","cbad"]
Output: 1
Explanation: 1 group ["abcd","cdab","adcb","cbad"]

'''




class Solution(object):
    def numSpecialEquivGroups(self, A):
        word_set = set()
        for word in A:
            oddpart = ''.join(sorted(word[0::2]))
            evenpart = ''.join(sorted(word[1::2]))
            word_set.add(oddpart + evenpart)
        return len(word_set)


'''
Idea/thoughts:
for each word in input list,
sort the even indices and make a string
sort odd indices and make a string
add the odd and even concatenation to a set.
Time-Complexity: O(len(A).n.log(n))

'''