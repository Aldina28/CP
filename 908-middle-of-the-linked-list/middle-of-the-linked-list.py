# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        if count%2 != 0:
            count = count//2+1
        else:
            count = count//2+1
        pos = 0
        current = head
        while pos<count-1 and current:
            pos+=1
            current = current.next
        return current