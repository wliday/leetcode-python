class Solution(object):
    def swapPairs(self, head):
        if not (head and head.next):
            return head

        second = head.next
        head.next = self.swapPairs(head.next.next)
        second.next = head
        return second
