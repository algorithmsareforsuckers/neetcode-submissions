# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # build lineage lists
        parents = {root.val : None}

        def lineage_dfs(r_root, l_root, parent) -> None:
            nonlocal parents

            if r_root:
                parents[r_root.val] = parent
                lineage_dfs(r_root.right, r_root.left, r_root)
            if l_root:
                parents[l_root.val] = parent
                lineage_dfs(l_root.right, l_root.left, l_root)
            
            return None
        
        def lineage_list(r) -> List:
            nonlocal parents
            res = [r]
            curr_parent = parents[r.val]
            node = r 
            while curr_parent:
                res.append(curr_parent)

                node = curr_parent
                curr_parent = parents[node.val]
            
            return res
        
        lineage_dfs(root.right, root.left, root)


        lin_p = lineage_list(p)
        lin_q = lineage_list(q)

        
        while lin_p and lin_q and lin_p[-1].val == lin_q[-1].val:
            curr = lin_p.pop()
            lin_q.pop()
            print(curr.val)
        
        
        return curr
                





            