def combinationSum( candidates, target):
    def backtrack(tmp, start, end, target):
        if target == 0:
            print("tmp",tmp[:])
            ans.append(tmp[:])
        elif target > 0:
            for i in range(start, end):
                tmp.append(candidates[i])
                backtrack(tmp, i, end, target - candidates[i])
                print("pop",tmp.pop())

    ans = []
    candidates.sort()
    backtrack([], 0, len(candidates), target)
    return ans

print(combinationSum([2,3,7],7))

answer = [[None] * 2 for _ in range(3)]
print(answer)