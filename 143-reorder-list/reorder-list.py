# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return 
        stack = []
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next
        curr = head
        n = len(stack)//2
        for i in range(n):
            temp = curr.next
            stack_elt = stack.pop() 
            curr.next = stack_elt
            stack_elt.next = temp
            curr = curr.next.next
        curr.next = None
