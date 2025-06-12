"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        queue = deque([node])
        clone = {node.val:Node(node.val, [])}
        while queue:
            root = queue.popleft()
            curr_clone = clone[root.val]
            for neighbor in root.neighbors:
                if neighbor.val not in clone:
                    clone[neighbor.val] = Node(neighbor.val, [])
                    queue.append(neighbor)
                curr_clone.neighbors.append(clone[neighbor.val])
        return clone[node.val]