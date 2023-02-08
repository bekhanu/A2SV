# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cat = ListNode(0, head)
        prev = head
        current = head.next
        
        
        while current:
            if current.val >= prev.val:
                prev = current
                current = current.next
                continue
                
                
            temp = cat
            while current.val > temp.next.val:
                temp = temp.next
            prev.next = current.next
            current.next = temp.next
            temp.next = current
            current= prev.next
        return cat.next
        
        