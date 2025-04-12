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
        hashMap={None:None}
        current = head
        while current:
            hashMap[current] = Node(current.val)
            current = current.next
        current = head
        while current:
            copy = hashMap[current]
            copy.next = hashMap[current.next]
            copy.random = hashMap[current.random]
            current = current.next
        return hashMap[head]
