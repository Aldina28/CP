# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.idx = len(postorder)-1
        hashMap = {n:i for i, n in enumerate(inorder)}
        def dfs(l, r):
            if l>r:
                return None
            hashMap_idx = hashMap[postorder[self.idx]]
            root = TreeNode(postorder[self.idx])
            self.idx-=1
            root.right = dfs(hashMap_idx+1, r)
            root.left = dfs(l, hashMap_idx-1)
            return root
        return dfs(0, len(inorder)-1)
            
