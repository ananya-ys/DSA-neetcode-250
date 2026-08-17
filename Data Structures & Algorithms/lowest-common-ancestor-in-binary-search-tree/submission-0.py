# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca = [root]
        def search(root) :
            if not root :
                return 0

            lca[0] = root
            if root is p or root is q :
                return
            elif p.val < root.val and q.val < root.val : 
                search(root.left) 
            elif p.val > root.val and q.val > root.val:
                search(root.right)
            else :
                return
        search(root)
        return lca[0]
