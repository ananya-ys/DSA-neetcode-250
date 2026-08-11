# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        large  = [0] 
        def height(root) :
            if not root :
                return 0
            
            lefth = height(root.left)
            righth = height(root.right)
            dia = lefth + righth

            large[0] = max(large[0], dia)
            return 1 + max(lefth , righth)

        height(root)
        return large[0]