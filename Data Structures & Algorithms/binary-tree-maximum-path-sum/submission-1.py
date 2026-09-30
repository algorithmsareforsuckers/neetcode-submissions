# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = float('-inf')
        def dfs(root):
            nonlocal best
            # Recursively find max weight paths
            if not root:
                return 0
            
            mleft = dfs(root.left)
            mright = dfs(root.right)

            tmp = root.val + max(0, mleft, mright)
            best = max(best, tmp, mleft + root.val + mright)

            return tmp
        
        dfs(root)
        return best
        
