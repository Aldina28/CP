# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = deque()
        queue.append(root)
        flip = True
        while queue:
            length = len(queue)
            temp = [0]*length
            for i in range(length):
                node = queue.popleft()
                index = i if flip else length-i-1
                temp[index] = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            flip = not flip
            result.append(temp)
        return result