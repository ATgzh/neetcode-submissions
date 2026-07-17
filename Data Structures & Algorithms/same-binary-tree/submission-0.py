# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dp(curr, now):
            if not curr and not now:
                return True
            if (curr and not now) or (not curr and now):
                return False
            if curr.val != now.val:
                return False
            
            return dp(curr.left, now.left) and dp(curr.right, now.right)
        
        return dp(p, q)
            