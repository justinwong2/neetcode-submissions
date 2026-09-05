# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class NodeWrapper:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        q = []
        currNode = ListNode()
        head = currNode
        for n in lists:
            if n is None:
                continue
            heapq.heappush(q, NodeWrapper(n))
        
        while q:
            currWrapper = heapq.heappop(q)
            currNode.next = currWrapper.node
            currNode = currNode.next
            currWrapper.node = currWrapper.node.next
            if currWrapper.node is not None:
                heapq.heappush(q, currWrapper)
        
        return head.next
        
        