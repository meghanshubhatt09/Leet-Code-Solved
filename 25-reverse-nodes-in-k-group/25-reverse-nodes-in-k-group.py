# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head == None or k == 1:
            return head
        
        dummyNode = ListNode(0,head)
        
        curr,nxt,prev = dummyNode,dummyNode,dummyNode
        count = 0
        
        while(curr.next != None):
            curr = curr.next 
            count+=1
            
        while(count >= k):
            curr = prev.next 
            nxt = curr.next 

            for i in range(1,k):
                
                curr.next = nxt.next 
                nxt.next = prev.next 
                prev.next = nxt 
                nxt = curr.next 
            
            count -= k
            prev = curr
        return dummyNode.next
        
        

                

                
            
        
        
        



                
                
        