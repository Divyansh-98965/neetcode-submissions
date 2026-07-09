# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        try:
            prev = None
            curr = head
            nextt   = head.next

            while curr is not None:
                curr.next = prev
                prev = curr
                curr = nextt
                if (nextt == curr) and (nextt == None):
                    break 
                else:
                    nextt = nextt.next

        
            return prev

        except AttributeError:
            return head