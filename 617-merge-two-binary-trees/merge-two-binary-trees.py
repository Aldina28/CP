# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root1, root2):
            if not root1 and not root2:
                return
            if not root2:
                return root1
            if not root1:
                return root2
            root = TreeNode(root1.val+root2.val)
            root.left = dfs(root1.left, root2.left)
            root.right = dfs(root1.right, root2.right)
            return root
        return dfs(root1, root2)
            
