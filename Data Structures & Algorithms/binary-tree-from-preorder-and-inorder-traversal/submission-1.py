# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_index = {value : i for i, value in enumerate(inorder)}
        pre_ind = 0

        def builder(pre_range, in_range):
            pre_start, pre_end = pre_range
            in_start, in_end = in_range
            if pre_start == pre_end: return None

            root_value = preorder[pre_start]
            res = TreeNode(val=root_value)

            i = in_index[root_value] # index in inorder
            left_size = i - in_start
            right_start = pre_start + 1 + left_size
            # build Left subtrees
            if i > 0:
                res.left = builder(
                    [pre_start + 1, right_start],
                    [in_start, i]
                )

            #build right subtrees
            if len(preorder) > i+1:
                res.right = builder(
                    [right_start, pre_end],
                    [i+1, in_end]
                )

            return res
        
        return builder([0, len(preorder)], [0, len(inorder)])
