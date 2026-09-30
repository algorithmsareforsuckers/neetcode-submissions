# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sub_dfs(root, subRoot):
            if (not subRoot) and (not root):
                return True
            if (not root) or (not subRoot) or (root.val != subRoot.val):
                return False
            
            left = sub_dfs(root.left, subRoot.left)
            right = sub_dfs(root.right, subRoot.right)

            return left and right

        stack = [root]
        node = root
        while stack:
            node = stack.pop()

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            
            if sub_dfs(node, subRoot):
                return True
        return False

