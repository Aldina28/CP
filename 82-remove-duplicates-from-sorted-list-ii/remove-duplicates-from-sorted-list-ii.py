# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        while curr:
            if curr.next and curr.next.val==curr.val:
                while curr.next and curr.next.val==curr.val:
                    curr = curr.next
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next
        return dummy.next
        # if not head or not head.next:
        #     return head
        # if head.val==head.next.val:
        #     while head.next and head.val==head.next.val:
        #         head=head.next
        #     return self.deleteDuplicates(head.next)
        # else:
        #     head.next = self.deleteDuplicates(head.next)
        #     return head
