# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        while curr and curr.next:
            temp = curr.next.next
            temp2 = curr.next

            temp2.next = curr
            curr.next = temp
            prev.next = temp2

            prev = curr
            curr = temp
        return dummy.next

