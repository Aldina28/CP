"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        cur1 = head

        dic = defaultdict()
        dic[None] = None
        while cur1:
            cur2 = Node(cur1.val)
            dic[cur1] = cur2
            cur1 = cur1.next

        cur1 = head
        while cur1:
            copy = dic[cur1]
            copy.next = dic[cur1.next]
            copy.random = dic[cur1.random]
            cur1 = cur1.next
        return dic[head]
