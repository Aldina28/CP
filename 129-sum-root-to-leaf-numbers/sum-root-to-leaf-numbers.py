# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def sums(root, result, temp):
            if not root:
                return
            temp = temp*10+root.val
            if not root.left and not root.right:
                result[0] += temp
                return 
            sums(root.left, result, temp)
            sums(root.right, result, temp)
        result = [0]
        temp = 0
        sums(root, result, temp)
        return result[0]
        