# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
            current1 = l1
            current2 = l2
            mergedFirst = None
            mergedLast = None
            
            if l1 and l2:
                if l1.val < l2.val:
                    mergedFirst = l1
                    current1 = l1.next
                else:
                    mergedFirst = l2
                    current2 = l2.next
            else:
                return l1 if l1 else l2
                
            mergedLast = mergedFirst
            
            while current1 and current2:
                if current1.val < current2.val:
                    mergedLast.next = current1
                    current1 = current1.next
                    mergedLast = mergedLast.next
                else:
                    mergedLast.next = current2
                    current2 = current2.next
                    mergedLast = mergedLast.next
                    
            if current1:
                mergedLast.next = current1
            else:
                mergedLast.next = current2
                    
            return mergedFirst