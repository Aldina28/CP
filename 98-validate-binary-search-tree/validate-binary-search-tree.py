# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.result = []
        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            self.result.append(node.val)
            inorder(node.right)
        inorder(root)
        for i in range(len(self.result)-1):
            if self.result[i]>=self.result[i+1]:
                return False
        return True