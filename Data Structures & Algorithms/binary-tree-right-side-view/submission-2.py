# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        arr = []
        q = deque()
        if root is None:
            return arr
        q.append(root)
        while len(q) > 0:
            origLen = len(q)
            for i in range(len(q)):
                node = q.popleft()
                if i + 1 == origLen:
                    arr.append(node.val)
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
        
        return arr

        