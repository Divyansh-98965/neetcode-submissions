# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool: 
        traversal_array = []
        # def preorder(t):
        #     if t is None:
        #         return root

        #     self.traversal_array.append(t.val)
        #     preorder(t.left)
        #     preorder(t.right)
        
        # preorder(root)

        # length = len(self.traversal_array)

        # for i in range(length - 2):
        """ wrong returns true after finding one case at top
        #     if self.traversal_array[i+1] <self.traversal_array[i]<self.traversal_array[i+2]:
        #         return True
        #     else:
        #         return False"""
        def inorder(t):
            if not t:
                return
            inorder(t.left)
            traversal_array.append(t.val)
            inorder(t.right)

        inorder(root)
        length = len(traversal_array)
        for i in range(1,length):
            if (traversal_array[i] <= traversal_array[i - 1]):
                return False
        return True
