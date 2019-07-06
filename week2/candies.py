class Solution(object):
    def distributeCandies(self, candies):
        total_candy = len(candies)
        candy_set = set(candies)
        candy_list = list(candy_set)
        if len(candy_set) >= total_candy / 2:
            return total_candy / 2
        else:
            # return len(candy_list+ candies[:(total_candy/2)-len(candy_list)])
            return len(candy_list)


'''
Ideas/thoughts:
Create a set and the sister will get half the len of candy list, if there are completely different varieties 
If not , then sister will get len of different candies.

'''