# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        d = deque([root])
        res = []
        curr = []
        l_num = 1
        next_num = 0

        while d:
            node = d.popleft()
            curr.append(node.val)

            if node.left:
                next_num += 1
                d.append(node.left)
            if node.right:
                next_num += 1
                d.append(node.right)
            
            l_num -= 1 # remove one from this layer's number.
            if l_num == 0:
                # layer over, append to res, and reset l_num and next_num
                res.append(curr)
                curr = []
                l_num = next_num
                next_num = 0
        
        return res




        