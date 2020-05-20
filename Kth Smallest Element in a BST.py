class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        arr=[]
        if not root:
            return 0
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            arr.append(root.val)
            dfs(root.right)
        dfs(root)
        print(arr)
        return arr[k-1]
