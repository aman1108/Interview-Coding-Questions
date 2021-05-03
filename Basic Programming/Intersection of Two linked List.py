# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodeA,nodeB=headA,headB
        cntA,cntB=0,0
        while(nodeA):
            cntA+=1
            nodeA=nodeA.next
        while(nodeB):
            cntB+=1
            nodeB=nodeB.next
        
        for i in range(cntA-cntB):
            headA=headA.next
        for i in range(cntB-cntA):
            headB=headB.next
        
        while(headA):
            if (headA==headB):
                return headA
            headA=headA.next
            headB=headB.next
        return 
