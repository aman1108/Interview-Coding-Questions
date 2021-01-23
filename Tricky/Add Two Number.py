#Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans=[]
        num1=0
        num2=0
        ctr=1
        while(l1!=None):
            num1=num1+(ctr*(l1.val))
            l1=l1.next
            ctr=ctr*10
        ctr=1
        while(l2!=None):
            num2=num2+(ctr*(l2.val))
            l2=l2.next
            ctr=ctr*10

        s=num1+num2
        L = ListNode()
        L.val=s%10
        v2=L
        s=s//10
        while(s!=0):
            v1= ListNode()
            v1.val=s%10
            v2.next=v1
            v2=v1
            s=s//10
        return L
            
            
        
            
        
