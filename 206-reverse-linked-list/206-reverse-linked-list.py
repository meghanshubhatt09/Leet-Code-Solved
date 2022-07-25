# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        curr = head
        nxt = curr
        
        if head == None:
            return None
        
        while curr.next != None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        curr.next = prev
        
        return curr
        
#         vals = []
#         curr = head
#         while curr:
#             vals.append(curr.val)
#             curr = curr.next
        
#         j = len(vals)-1
#         curr = head
#         while curr:
#             curr.val = vals[j]
#             j-=1
#             curr = curr.next
#         return head


        
            
        