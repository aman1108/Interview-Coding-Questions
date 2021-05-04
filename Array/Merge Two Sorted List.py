# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (l1==None and l2==None):
            return 
        node=ListNode()
        val=node
        while (l1 and l2):
            if (l1.val<=l2.val):
                node.val=l1.val
                node.next=ListNode()
                node=node.next
                l1=l1.next
            else:
                node.val=l2.val
                node.next=ListNode()
                node=node.next
                l2=l2.next
        if (l1):
            node.val=l1.val
            node.next=l1.next
        if (l2):
            node.val=l2.val
            node.next=l2.next
        return val
        
