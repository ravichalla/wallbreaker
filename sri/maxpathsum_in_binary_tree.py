

# O(n) time | O(Log(n)) space
def maxPathSum(tree):
    _, maxSum =findMaxSum(tree)
    return maxSum

def findMaxSum(tree):
    if tree is None:
        return (0, 0)

    leftMaxSumAsBranch, leftMaxPathSum = findMaxSum(tree.left)
    rightMaxSumAsBranch, rightMaxPathSum  = findMaxSum(tree.right)
    # this could be negative
    maxChildSumAsBranch = max(leftMaxSumAsBranch, rightMaxSumAsBranch)

    value = tree.value
    maxSumAsBranch = max(maxChildSumAsBranch+value, value)
    maxSumAsRootNode = max(leftMaxSumAsBranch+ value + rightMaxSumAsBranch )
    maxPathSum = max(leftMaxPathSum, rightMaxPathSum, maxSumAsRootNode)

    return (maxSumAsBranch, maxPathSum)
