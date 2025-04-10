# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        listt = []
        while head:
            listt.append(head.val)
            head = head.next
        n = len(listt)
        k = k % n
        count = 0
        while count < k:
            temp = listt[-1]  
            for i in range(len(listt)-1, 0, -1):
                listt[i] = listt[i-1]  
            listt[0] = temp
            count+=1
        dummy = ListNode(0)
        current = dummy
    
        for val in listt:
            current.next = ListNode(val)
            current = current.next
        
        return dummy.next
        
