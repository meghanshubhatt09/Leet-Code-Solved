# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if len(lists) == 0:
            return None
        
        result = []
        
        for i in (lists):
            
            curr = i
            while curr:
                result.append(curr.val)
                curr = curr.next
                
        result.sort()
    
        
        if len(result) == 1:
            return ListNode(result[0])
        
        
        prev = None
        head = None
        
        i = 0
        while(i<len(result)):
            node = ListNode(result[i])
            if prev == None:
                prev = node
                head = node
            else:
                prev.next = node
                prev = node
            i+=1
            
        return head

        
    
        