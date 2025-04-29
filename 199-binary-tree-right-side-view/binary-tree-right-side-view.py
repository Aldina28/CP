# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def bfs(root, depth):
            if root:
                if len(result) == depth:
                    result.append(root.val)
                bfs(root.right, depth+1)
                bfs(root.left, depth+1)
        result = []
        bfs(root, 0)
        return result
            