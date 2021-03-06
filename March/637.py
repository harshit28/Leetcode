# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        res=[]
        if not root: return res
        q=[root]
        while q:
            q1=[]
            total=0
            cnt=0
            while q:
                node =q.pop()
                if node.left: q1.append(node.left)
                if node.right: q1.append(node.right)
                total+=node.val
                cnt+=1
            res.append(total*1.0/cnt)
            q=list(q1)
