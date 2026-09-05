# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        middle = slow
        after_middle = middle.next
        middle.next = None
        currNode = after_middle
        prevNode = None
        while currNode is not None:
            temp = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = temp

        new_head = head
        while new_head is not None and prevNode is not None:
            temp1 = new_head.next
            temp2 = prevNode.next
            new_head.next = prevNode
            prevNode.next = temp1
            new_head = temp1
            prevNode = temp2
