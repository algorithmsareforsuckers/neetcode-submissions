# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # for DFS, we should keep track of the right mode node that we've seen at each depth
        if not root:
            return []
        rightmost = [] # first is depth 0 (i.e. root), then 1, then 2, ...

        stack = [[root, 0]]

        while stack:
            node, depth = stack.pop()

            if len(rightmost) <= depth:
                rightmost.append(node.val)
            else:
                # We add in left to right order, so whenever we 
                # see a new val at a depth it's the rightmost we've seen
                rightmost[depth] = node.val 
            
            if node.right: stack.append([node.right, depth + 1])
            if node.left: stack.append([node.left, depth + 1])
        
        return rightmost
