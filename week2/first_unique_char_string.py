from collections import Counter


class Solution(object):
    def firstUniqChar(self, s):
        cntr = Counter(s)
        print(cntr)
        for index, char in s:
            if cntr[char] == 1:
                return index
            else:
                continue
        return -1


'''
Ideas/thoughts:
iterate thorough the string itself, and return index or -1 accordingly

'''