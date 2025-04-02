# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ptr_a = headA
        ptr_b = headB

        # while ptr_a!=ptr_b:
        #     ptr_a = ptr_a.next if ptr_a else headB
        #     ptr_b = ptr_b.next if ptr_b else headA
        # return ptr_b
        sett = set()

        while headA:
            sett.add(headA)
            headA = headA.next
        while headB:
            if headB in sett:
                return headB
            headB = headB.next
        return None