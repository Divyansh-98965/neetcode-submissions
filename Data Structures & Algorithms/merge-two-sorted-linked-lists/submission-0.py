# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #creating a dummy node to make a new list 
        dummy = ListNode(0)
        #using a second pointer to traverse along the
        # list so we can return from the first one
        tail = dummy

        # loop till both are not null
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            #only two cases possible
            else:
                tail.next = list2
                list2 = list2.next
            #move tail pointer to next node for comparison
            tail = tail.next

        # till list one node if loop ends before due to list finishing 
        #and add leftover node
        tail.next = list1 if list1 else list2

        return dummy.next # return what's just next to 0 node