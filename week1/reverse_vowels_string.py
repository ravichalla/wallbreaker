'''
QUESTIONS:

345. Reverse Vowels of a String
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"

'''


class Solution(object):
    def reverseVowels(self, s):
        l_idx = 0
        r_idx = len(s) - 1
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        s_lst = list(s)
        while (l_idx < r_idx):
            if s_lst[l_idx] not in vowels:
                l_idx += 1
                continue
            if s_lst[r_idx] not in vowels:
                r_idx -= 1
                continue
            if s_lst[l_idx] in vowels and s_lst[r_idx] in vowels:
                s_lst[l_idx], s_lst[r_idx] = s_lst[r_idx], s_lst[l_idx]
                l_idx += 1
                r_idx -= 1
        return "".join(s_lst)


'''
Ideas/thoughts:
convert str to list 
take two pointers, left and right, check if left index value doesn't contains vowel,
right index value doesn't contain vowel and 
ifn't then interchange the values using pair interchange .
return list to str


'''