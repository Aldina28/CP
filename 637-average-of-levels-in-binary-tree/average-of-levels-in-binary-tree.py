# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        temp = 0
        count = 0
        current_depth = 0
        if not root:
            return 
        stack = deque()
        stack.append((root,0))
        while stack:
            node, depth = stack.popleft()
            if node:
                if depth != current_depth:
                    result.append(temp / count)  
                    temp = 0
                    count = 0
                    current_depth = depth
                temp += node.val
                count += 1
                if node.left:
                    stack.append((node.left, depth+1))
                if node.right:
                    stack.append((node.right, depth+1))
        if count != 0:
            result.append(temp / count)
        return result