# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        from collections import deque
        q = deque()
        if root is None:
            return root
        q.append(root)
        while q:
            currNode = q.popleft()
            currLeft = currNode.left
            currRight = currNode.right
            if currRight is not None:
                q.append(currRight)
            if currLeft is not None:
                q.append(currLeft)
            currNode.left = currRight
            currNode.right = currLeft
        
        return root
        