# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder = deque(preorder)
        def build(preorder, inorder):
            if inorder:
                index = inorder.index(preorder.popleft())
                root = TreeNode(inorder[index])
                root.left = build(preorder, inorder[:index])
                root.right = build(preorder, inorder[index+1:])
                return root
        return build(preorder, inorder)