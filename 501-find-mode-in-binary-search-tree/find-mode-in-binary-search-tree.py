# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.mp = {}

    def isValid(self, root):
        if root is None:
            return

        self.isValid(root.left)  
        self.mp[root.val] = self.mp.get(root.val, 0) + 1  
        self.isValid(root.right)  

    def findMode(self, root):
        self.isValid(root) 

        maxi = 0
        for value in self.mp.values():
            maxi = max(maxi, value)

        ans = []
        for key, value in self.mp.items():
            if value == maxi:
                ans.append(key)

        return ans