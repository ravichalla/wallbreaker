def permute( nums):
    def backtrack(start, end):
        if start == end:
            #print("start end equal",nums)
            ans.append(nums[:])
        for i in range(start, end):
            nums[start], nums[i] = nums[i], nums[start]
            #print("before backtrack",nums)
            backtrack(start + 1, end)
            #print("after backtrack",nums)
            nums[start], nums[i] = nums[i], nums[start]
        #print("forloop final",nums)

    ans = []
    backtrack(0, len(nums))

    return ans

#permute([1,2,3])
print(permute([1,2,3]))
# [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]] nums
#[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]] nums[:]
