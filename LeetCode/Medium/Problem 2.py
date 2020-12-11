# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        resHead = ListNode()
        resTracker = resHead
        carry = 0
        crit = l1.next or l2.next or l1.val or l2.val or carry
        
        while crit:
            tempSum = (l1.val if l1.val > 0 else 0) + (l2.val if l2.val > 0 else 0) + carry
            resTracker.val = tempSum % 10
            carry = 1 if tempSum >= 10 else 0
            if(l1.next):
                l1 = l1.next
            else:
                l1.val = 0
            if(l2.next):
                l2 = l2.next
            else:
                l2.val = 0
            crit = l1.next or l2.next or l1.val or l2.val or carry
            if crit:
                resTracker.next = ListNode()
                resTracker = resTracker.next
            
        return resHead