# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is not None and q is None:
            return False
        elif p is None and q is not None:
            return False
        from collections import deque
        q1 = deque()
        q2 = deque()
        q1.append(p)
        q2.append(q)

        while q1 and q2:
            currP = q1.popleft()
            currQ = q2.popleft()
            if currP is None and currQ is None:
                continue
            elif currP is not None and currQ is None:
                return False
            elif currP is None and currQ is not None:
                return False
            elif currP.val != currQ.val:
                return False
            q1.append(currP.left)
            q1.append(currP.right)
            q2.append(currQ.left)
            q2.append(currQ.right)
        
        if len(q1) != len(q2):
            return False
        return True
            
