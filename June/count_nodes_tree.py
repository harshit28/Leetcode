# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root,count=0):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        count=1
        
    
        if root.left:
            count+=self.countNodes(root.left)
        
        if root.right:
            count+=self.countNodes(root.right)
        
        return count
        
