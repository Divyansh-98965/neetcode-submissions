# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        # finding the size of linked_list
        n = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next 
        slow.next = None


        #taking pointer to next half of list and reversing it
        prev = None
        curr = second
        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt
        
        p1 = head
        p2 = prev
        while p2:
            tmp1 = p1.next 
            tmp2 = p2.next 

            p1.next = p2
            p2.next = tmp1

            p2 = tmp2
            p1 = tmp1


