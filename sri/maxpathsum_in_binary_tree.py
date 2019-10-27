class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

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

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None
    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

print(maxPathSum(stringToTreeNode("1,2,3,4,5,6,7,8")))