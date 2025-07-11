# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        # dummy = ListNode(0, head)
        # current = dummy
        # while current and current.next:
        #     if current.next.val == val:
        #         current.next = current.next.next
        #     else:
        #         current = current.next
        # return dummy.next 
        dummy = ListNode(0, head)
        curr = dummy
        while curr:
            while curr.next and curr.next.val == val:
                curr.next = curr.next.next
            curr = curr.next
        return dummy.next
        