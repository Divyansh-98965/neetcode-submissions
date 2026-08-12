"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        hash_table = dict()
        pointer = head
        # traverse the original linked list to store values of pointer corresponding to the nodes
        while pointer is not None:
            hash_table[pointer] = Node(pointer.val)
            pointer = pointer.next
        
        pointer = head
        
        while pointer is not None:
            newNode = hash_table[pointer]
            newNode.next = hash_table.get(pointer.next)
            newNode.random = hash_table.get(pointer.random)
            pointer = pointer.next

        return hash_table.get(head)
