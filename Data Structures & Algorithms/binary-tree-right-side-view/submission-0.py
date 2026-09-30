# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS but only keep 1 value per level
        if not root:
            return []
        res = []

        q = collections.deque([root])

        while q:
            res.append(q[0].val) # we will append values per level from right to left

            for _ in range(len(q)):
                node = q.popleft()
                if node.right: q.append(node.right)
                if node.left: q.append(node.left)
        
        return res