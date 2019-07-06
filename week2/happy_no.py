
def isHappy( n):
    set_no = set()
    while n!=1:
        if n in set_no:
            return False
        set_no.add(n)
        n= sum([int(i)**2 for i in str(n)])
    else:
        return  True
print(isHappy(19)) # true
print(isHappy(3))   # false

'''
Ideas/thoughts:
If n is 1,directly true
else, make n , sum of square of each digits
as want to kept in while loop, will make a set and add the n values,
so that it won't loop, with same n's.

'''