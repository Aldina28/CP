# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # values = []
        # curr = head
        # while curr:
        #     values.append(curr.val)
        #     curr = curr.next
        # curr = head
        # while curr and curr.val == values.pop():
        #     curr = curr.next
        # return curr is None
        # values = []
        # while head:
        #     values.append(head.val)
        #     head = head.next
        # l, r = 0, len(values)-1
        # while l<r:
        #     if values[l]!=values[r]:
        #         return False
        #     l+=1
        #     r-=1
        # return True

        
        list1 = []
        while head:
            list1.append(head.val)
            head = head.next
        
        return list1 == list1[::-1]