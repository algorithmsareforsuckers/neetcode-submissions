# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # we want to add all of the roots to a queue / stack (not sure yet)
        # so that they end up in the list in a sorted manner.
        if not root:
            return -1

        keep = collections.deque()
        def dfs(root):
            if not root:
                return []
            
            pl, pr = [], []
            if root.left: pl = dfs(root.left)
            if root.right: pr = dfs(root.right)

            return pl + [root] + pr
        
        std = dfs(root)
        return std[k-1].val
        