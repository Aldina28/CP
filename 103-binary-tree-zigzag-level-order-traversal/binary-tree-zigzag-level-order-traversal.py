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
        level = 0
        result = []
        queue = deque([root])
        while queue:
            temp = []
            level+=1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    temp.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            if level%2!=0:
                result.append(temp)
            else:
                result.append(temp[::-1])
        return result