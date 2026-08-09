# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if the tree is empty, return null
        if not root:
            return None
        # initialize a queue and insert the root node
        queue = deque([root])
        while queue: 
            node= queue.popleft()
            node.left, node.right = node.right, node.left
            # if the left child exist, add it to the queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root
