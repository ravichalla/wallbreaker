class Solution(object):
    def uncommonFromSentences(self, A, B):

        bothlists= A.split(" ")+B.split(" ")
        return [word for word in bothlists if bothlists.count(word)==1]

'''
Ideas/thoughts:
split the two lists and concatenate, 
and check for each word if count is 1
'''