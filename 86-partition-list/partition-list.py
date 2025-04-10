# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small_ll, big_ll = ListNode(), ListNode()
        small_ptr, big_ptr = small_ll, big_ll

        while head:
            if head.val<x:
                small_ptr.next = head
                small_ptr = small_ptr.next
            else:
                big_ptr.next = head
                big_ptr = big_ptr.next
            head = head.next
        small_ptr.next = big_ll.next
        big_ptr.next = None
        return small_ll.next
        
        