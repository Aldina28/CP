# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([root])
        most_freq = defaultdict(int)
        while queue:
            node = queue.popleft()
            most_freq[node.val]+=1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        modes = []
        max_count = max(most_freq.values())
        for key, val in most_freq.items():
            if val == max_count:
                modes.append(key)
        return modes