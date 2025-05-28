# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.index = len(postorder)-1
        index_map = {val:i for (i, val) in enumerate(inorder)}
        def build(l, r):
            if l>r:
                return None
            root_val = postorder[self.index]
            root = TreeNode(root_val)
            root_idx = index_map[root_val]
            self.index-=1
            root.right = build(root_idx+1, r)
            root.left = build(l, root_idx-1)
            return root
        return build(0, len(postorder)-1)
