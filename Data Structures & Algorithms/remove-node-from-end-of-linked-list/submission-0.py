# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]: 
        pointer = head
        k = 0
        while pointer:
            pointer = pointer.next 
            k += 1

        if k == n:
            head = head.next
            return head
        elif k > n:
            pointer2 = head
            for i in range(k - n - 1):
                pointer2 = pointer2.next
                
            pointer2.next = pointer2.next.next
            return head