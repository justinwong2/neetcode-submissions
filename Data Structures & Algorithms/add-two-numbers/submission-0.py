# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tempNode = ListNode()
        head = tempNode
        carryOver = 0

        while l1 is not None and l2 is not None:
            value = carryOver + l1.val + l2.val
            if value >= 10:
                carryOver = value // 10
                value = value - (carryOver * 10)
            else:
                carryOver = 0
            tempNode.next = ListNode(value)
            tempNode = tempNode.next
            l1 = l1.next
            l2 = l2.next
        
        while l1 is not None:
            value = carryOver + l1.val
            if value >= 10:
                carryOver = value // 10
                value = value - (carryOver * 10)
            else:
                carryOver = 0
            tempNode.next = ListNode(value)
            tempNode = tempNode.next
            l1 = l1.next

        while l2 is not None:
            value = carryOver + l2.val
            if value >= 10:
                carryOver = value // 10
                value = value - (carryOver * 10)
            else:
                carryOver = 0
            tempNode.next = ListNode(value)
            tempNode = tempNode.next
            l2 = l2.next
        if carryOver != 0:
            tempNode.next = ListNode(carryOver)
            tempNode = tempNode.next
        return head.next
        