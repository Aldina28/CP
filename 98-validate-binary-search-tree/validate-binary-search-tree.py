# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root, left, right):
            if not root:
                return True
            if left<root.val<right:
                ll = valid(root.left, left, root.val)
                rr = valid(root.right, root.val, right)
                return ll and rr
            else:
                return False
        return valid(root, -float('inf'), float('inf'))