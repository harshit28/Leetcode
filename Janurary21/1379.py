def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
  self.ans = None
  def dfs(node):
      if node:
          if node.val == target.val:
              self.ans=node
              return
          dfs(node.left)
          dfs(node.right)
  dfs(cloned)
  return self.ans
