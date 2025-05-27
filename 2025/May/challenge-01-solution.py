"""
Challenge 01 – Reverse a Linked List
Replace `pass` with your code. Submit via pull-request.
"""
class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val, self.next = val, nxt

def reverse_list(head: ListNode) -> ListNode:
    prev, cur = None, head
    while cur:
        cur.next, prev, cur = prev, cur, cur.next
    return prev
