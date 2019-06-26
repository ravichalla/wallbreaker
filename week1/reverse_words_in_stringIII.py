'''
QUESTION:
557. Reverse Words in a String III
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
'''


class Solution(object):
    def reverseWords(self, s):
        word_lst = s.split(" ")
        for index, word in enumerate(word_lst):
            word_lst[index] = word[::-1]
        word_lst = " ".join(word_lst)
        return word_lst

'''
Ideas/thoughts:
split the words in the sentence into a list 
and reverse the words individually
join the reversed list


'''

