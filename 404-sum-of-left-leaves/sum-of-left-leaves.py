# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 0
        if root.left and not root.left.left and not root.left.right:
            res+=root.left.val
        res+=self.sumOfLeftLeaves(root.left)
        res+=self.sumOfLeftLeaves(root.right)
        return res