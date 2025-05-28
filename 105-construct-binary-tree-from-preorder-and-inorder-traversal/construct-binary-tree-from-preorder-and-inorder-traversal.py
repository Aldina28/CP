# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.index = 0 

        idxMap = {val: i for (i, val) in enumerate(inorder)}


        def build(l, r): 

            if l > r : 
                return None 
    
            
            rootVal = preorder[self.index]
            root = TreeNode(rootVal)
            idx = idxMap[rootVal]
            self.index += 1

            root.left = build(l, idx - 1)
            root.right = build(idx + 1, r)
            return root
        
        return build(0, len(preorder) - 1)