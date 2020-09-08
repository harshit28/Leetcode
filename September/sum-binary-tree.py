# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        # arr=[]
        self.ans = 0
        def dfs(node,arr):
            if node:
                print(arr)
                arr.append(str(node.val))
                if not node.left and not node.right:
                    self.ans+=int("".join(arr),2)
                dfs(node.left,arr)
                dfs(node.right,arr)
                arr.pop()
        dfs(root,[])
        return self.ans