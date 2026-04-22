# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        curr = head

        while curr:
            # save next node before we break the link
            temp = curr.next

            # reverse the link
            curr.next =prev

            #move the pointer forward
            prev = curr
            curr =temp

        return prev # new head