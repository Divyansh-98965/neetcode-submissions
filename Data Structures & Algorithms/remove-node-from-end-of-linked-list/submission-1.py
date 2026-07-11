# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]: 
    #     usingf conditions to check for edge case
    #     pointer = head
    #     k = 0
    #     while pointer:
    #         pointer = pointer.next 
    #         k += 1
    # # Edge case in which we have to delete the first node
    #     if k == n:
    #         head = head.next
    #         return head
    #     # k must always be greater than n size of list
    #     elif k > n:
    #         pointer2 = head
    #         for i in range(k - n - 1):
    #             pointer2 = pointer2.next
                
    #         pointer2.next = pointer2.next.next
    #         return head

    #     without using conditionals 
        dummy = ListNode(0,head)
        left = dummy
        right = dummy
        for i in range(n + 1):
            right = right.next

        while right is not None:
            left = left.next
            right = right.next 

        left.next = left.next.next 

        return dummy.next 