# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        list1 = []
        while head:
            list1.append(head.val)
            head = head.next
        
        return list1 == list1[::-1]

        