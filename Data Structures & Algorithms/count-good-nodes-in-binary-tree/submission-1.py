# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        # DFS and maintain the largest value seen at the current depth
        def dfs(root, mx):
            if not root:
                return 0
            ret = 0
            if root.val >= mx:
                mx = root.val
                ret += 1
            
            return ret + dfs(root.left, mx) + dfs(root.right, mx)

        return dfs(root, float('-inf'))