# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def bala(p,q) :
            if not p and not q :
                return True
            if (p and not q) or (q and not p) :
                return False 
            if p.val != q.val :
                return False 

            return bala(p.left , q.left) and bala(p.right, q.right)
        return bala(p,q)
