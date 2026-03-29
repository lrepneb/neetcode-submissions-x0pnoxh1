# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def match(root, subRoot):
            if not subRoot and not root:
                return True
            if root and subRoot and root.val == subRoot.val:
                return match(root.left, subRoot.left) and match(root.right, subRoot.right)
            return False
            

        if not root:
            return False
        if not subRoot:
            return True
        
        if match(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
