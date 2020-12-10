# https://leetcode.com/problems/reverse-linked-list/

# Attempt 1 - Iterative Solution

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr:
            nxt_temp = curr.next
            curr.next = prev
            prev = curr
            curr = nxt_temp
        return prev