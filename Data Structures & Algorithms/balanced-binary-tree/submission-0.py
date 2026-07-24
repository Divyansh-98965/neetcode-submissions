# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanceFactor = 0
        def height(head):
            if head is None:
                return 0
            
            lheight = height(head.left)
            rheight = height(head.right)
            self.balanceFactor = max(self.balanceFactor, abs(lheight - rheight))

            return 1 + max(lheight,rheight)

        height(root)
        if (root is None) or (self.balanceFactor <= 1): 
            return True

        return False
        
