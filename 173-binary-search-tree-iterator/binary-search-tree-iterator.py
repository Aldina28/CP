# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root):
        self.out=[]
        def inorder(r):
            if not r:
                return
            inorder(r.left)
            self.out.append(r.val)
            inorder(r.right)
        inorder(root)
        self.index=0
        
    def next(self):
        self.index+=1
        return self.out[self.index-1]
        
    def hasNext(self):
        return self.index<len(self.out)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()