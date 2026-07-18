# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameter = 0
        def height(node):
            if node is None:
                return 0
            #calculate height at each node
            lheight = height(node.left)
            rheight = height(node.right)

            self.maxDiameter =  max(self.maxDiameter,lheight + rheight)

            return 1 + max(lheight,rheight)

        height(root)
        return self.maxDiameter

        
