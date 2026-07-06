# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # define dfs(node,curSum) that return whther a valid path exist from this node
        def dfs(node,curSum):
            # if node is null, return false
            if not node:
                return False

            # add node.val to curSum
            curSum += node.val

            # if node is a leaf(no childerd), return whether curSumc == targetSum
            if not node.left and not node.right:
                return curSum == targetSum
            #  otherwise recrusively check the left and right subtree, returning true
            # if either has a valid path
            return dfs(node.left, curSum) or dfs(node.right, curSum)

            # call dfs(root, 0) to start search
        return dfs(root, 0)
            
