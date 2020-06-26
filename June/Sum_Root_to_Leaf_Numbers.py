class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        def dfs(node,arr):
            if node:
                 arr.append(str(node.val))
                 if not node.left and not node.right:   
                    self.ans+=int("".join(arr))
            if node.left:
                dfs(node.left,arr)
            if node.right:
                dfs(node.right,arr)
            arr.pop()
        self.ans=0
        dfs(root,[])
        return self.ansSum Root to Leaf Numbers
