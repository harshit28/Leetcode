class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:

        slist=[]
        
        def dfs(node):
            if not node:
                return None
            dfs(node.left)
            slist.append(node.val)
            dfs(node.right)
        if root1:    
            dfs(root1)
        if root2:
            dfs(root2)
        
        return sorted(slist)