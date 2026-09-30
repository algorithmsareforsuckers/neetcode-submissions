# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        stack = [root]
        mp = {None: (0,0)} #height, diameter

        while stack:
            curr = stack[-1]

            if curr.left and curr.left not in mp:
                stack.append(curr.left)
            elif curr.right and curr.right not in mp:
                stack.append(curr.right)
            else:
                curr = stack.pop()

                height = 1 + max(mp[curr.left][0], mp[curr.right][0])
                diameter = max(mp[curr.left][0] + mp[curr.right][0], mp[curr.left][1], mp[curr.right][1])
                mp[curr] = (height, diameter)
        
        return mp[root][1]

            


            