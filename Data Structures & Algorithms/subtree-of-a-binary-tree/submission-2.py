# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Create strings to represent the trees
        stack = [root]
        s_root = ""
        while stack:
            node = stack.pop()
            s_root += str(node.val)

            if node.right:
                stack.append(node.right)
            else:
                s_root += "|"
            if node.left:
                stack.append(node.left)
            else:
                s_root += "|"
            
        #s_root += "#"
        
        stack = [subRoot]
        s_sroot = ""
        while stack:
            node = stack.pop()

            s_sroot += str(node.val)
            if node.right:
                stack.append(node.right)
            else:
                s_sroot += "|"
            if node.left:
                stack.append(node.left)
            else:
                s_sroot += "|"
            
        #s_sroot += "#"

        print(s_root, s_sroot)
        
        if not s_root:
            if not s_sroot:
                return True
            return False
        
        return s_sroot in s_root
            

