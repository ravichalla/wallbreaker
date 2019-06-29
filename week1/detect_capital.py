'''
QUESTION:
520. Detect Capital

Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.


Example 1:

Input: "USA"
Output: True


Example 2:

Input: "FlaG"
Output: False


Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.



'''


class Solution(object):
    def detectCapitalUse(self, word):
        return word.isupper() or word.islower() or self.isTitle(word)

    def isTitle(self, word):
        return word[0].isupper() and word[1:].islower()


'''
Ideas/thoughts:
check 3 scenarios , title, upper,lower.

'''