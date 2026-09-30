# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root: return ""
        res = []
        q = deque([root])
        while q:
            node = q.popleft()
            if not node: 
                res.append("n")
                continue
            res.append(str(node.val))

            q.append(node.left)
            q.append(node.right)
        
        return ",".join(res)
        

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "" or data == "n": return None
        nodes = data.split(",")

        head = TreeNode(val=int(nodes[0]))
        q,i = deque([head]), 1
        while q:
            curr = q.popleft()

            if nodes[i] != "n":
                curr.left = TreeNode(val=int(nodes[i]))
                q.append(curr.left)
            if nodes[i+1] != "n":
                curr.right = TreeNode(val=int(nodes[i+1]))
                q.append(curr.right)
            i += 2
        
        return head
