# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr,prev,head = None, None, None
        
        while(list1!=None and list2!=None):
            
            if list1.val < list2.val:
                curr = ListNode(list1.val)
                list1 = list1.next
                
            elif list1.val > list2.val:
                curr = ListNode(list2.val)
                list2 = list2.next
                
            else:
                curr = ListNode(list1.val)
                list1 = list1.next
                
            if prev == None:
                prev = curr
                head = curr
            else:
                prev.next = curr
                prev = curr
                
        if list1 != None:
            while(list1 != None):
                curr = ListNode(list1.val)
                if prev == None:
                    prev = curr
                    head = curr
                else:
                    prev.next = curr
                    prev = curr
                list1 = list1.next
        if list2 != None:
            while(list2 != None):
                curr = ListNode(list2.val)
                if prev == None:
                    prev = curr
                    head = curr
                else:
                    prev.next = curr
                    prev = curr
                list2 = list2.next
            
        return head
    
            
            
                
            
        