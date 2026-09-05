# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        highest = 0

        def dfs(node):
            nonlocal highest
            if node is None:
                return 0
            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)
            maxHeight = 1 + max(leftHeight, rightHeight)
            highest = max(highest, leftHeight + rightHeight)
            return maxHeight
        dfs(root)
        return highest
        