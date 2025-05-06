# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        inorderNodes = []
        minDiff = float("inf")

        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            inorderNodes.append(node.val)    # add val in sorted order
            inorder(node.right)
        
        inorder(root)

        for i in range(len(inorderNodes) -1):
            curDiff = inorderNodes[i+1] - inorderNodes[i]
            minDiff = min(minDiff, curDiff)

        return minDiff

