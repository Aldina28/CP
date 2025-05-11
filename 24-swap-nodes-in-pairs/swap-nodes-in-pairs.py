# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(None, head)
        prev = dummy

        while head and head.next:
            first = head
            second = head.next
            third = second.next

            prev.next = second
            second.next = first
            first.next = third

            prev = first
            head = third
        return dummy.next




