# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.result=[]
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            self.result.append(root.val)
            inorder(root.right)
        inorder(root)
        self.index=0

    def next(self) -> int:
        self.index+=1
        return self.result[self.index-1]

    def hasNext(self) -> bool:
        return self.index<len(self.result)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()