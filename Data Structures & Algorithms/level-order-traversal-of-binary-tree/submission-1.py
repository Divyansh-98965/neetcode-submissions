# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        # using a queue to push children into after popping the top element
        queue = deque([root])
        result_array = []
        
        while queue:
            lenq = len(queue)
            curr_level_nodes = []
            
            for _ in range(lenq):
                node = queue.popleft()
                curr_level_nodes.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            
            result_array.append(curr_level_nodes)
        return result_array
                        