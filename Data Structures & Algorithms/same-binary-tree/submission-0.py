# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def comp_dfs(p, q):
            if (not p) and (not q):
                return True
            if (not p) or (not q):
                return False
            
            if p.val != q.val:
                return False
            
            # Check if left and right subtrees are the same
            right = comp_dfs(p.right, q.right)
            left = comp_dfs(p.left, q.left)

            return left and right
        
        return comp_dfs(p, q)
