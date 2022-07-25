# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next
        
        j = len(vals)-1
        curr = head
        while curr:
            curr.val = vals[j]
            j-=1
            curr = curr.next
        return head
            
        