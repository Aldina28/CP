# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = root
        right = root
        height_l = 0
        height_r = 0
        while left:
            height_l+=1
            left = left.left
        while right:
            height_r+=1
            right = right.right
        if height_l==height_r:
            return pow(2, height_l)-1
        return 1+self.countNodes(root.left)+self.countNodes(root.right)