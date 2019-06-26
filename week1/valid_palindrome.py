'''
QUESTION:
125. Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false

'''

class Solution(object):
    def isPalindrome(self, s):
        char_list = []
        for c in s:
            if c.isalnum():
                char_list.append(c)
        left_index = 0
        right_index = len(char_list) - 1
        while (left_index < right_index):
            if char_list[left_index].upper() != char_list[right_index].upper():
                return False
            else:
                left_index += 1
                right_index -= 1
        return True


'''
Ideas/thoughts:
make a lst with the characters adding only alphanum
check if the left and right characters are equal

'''