# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        result = []
        carry = 0
        
        curr,prev,head = None,None,None
        
        
        while(l1 != None and l2 != None):
            curr_sum = l1.val + l2.val + carry
            carry = curr_sum//10
            curr = ListNode(curr_sum%10)
            
            if prev == None:
                prev = curr
                head = curr
            else:
                prev.next = curr
                prev = curr 
                
            l1 = l1.next
            l2 = l2.next
        
        if l1 != None:
            while(l1 != None):
                curr_sum = l1.val + carry
                carry = curr_sum//10
                curr = ListNode(curr_sum%10)
                prev.next = curr
                prev = curr 
                
                l1 = l1.next
            
        if l2 != None:
            while(l2 != None):
                curr_sum = l2.val + carry
                carry = curr_sum//10
                curr = ListNode(curr_sum%10)
                prev.next = curr
                prev = curr 
                
                l2 = l2.next
        
        if carry != 0:
            curr = ListNode(carry)
            prev.next = curr
            prev = curr 
            
        return head
    
 
        
        