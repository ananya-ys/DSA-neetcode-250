# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        bala = [True]
        def height(root) :
            if not root :
                return 0
            
            lefth = height(root.left)
            if bala[0] is False :
                return 0
            righth = height(root.right)

            if abs(lefth-righth) > 1 :
                bala[0] = False
                return 0

            return 1 + max(lefth, righth)
        height(root)
        return bala[0]
