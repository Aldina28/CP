# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return 
        stack = []
        stack.append(root)
        curr = root
        while stack:
            node = stack.pop()
            if node!=root:
                curr.right = node
                curr.left = None
            curr = node
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return root
        