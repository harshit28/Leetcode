class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.currentval = 0
        output = TreeNode()
        def dfs(node):
            if not node:
                return None
            dfs(node.right)
            self.currentval+=node.val
            node.val = self.currentval
            dfs(node.left)
            return node    
        return dfs(root)
