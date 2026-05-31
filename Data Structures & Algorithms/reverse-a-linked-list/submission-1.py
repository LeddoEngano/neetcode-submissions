# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        # 1,2 2,3 3,4 4,5 5,None
        # nxt:2 prev:1 curr.next:2 
        
        # 1 2 3 4 5
        # 5 4 3 2 1 

        # curr.next = None
        # curr.prev = 2
        # curr = 2


        while curr != None:
            nxt = curr.next
            curr.next = prev

            prev = curr
            curr = nxt

        return prev