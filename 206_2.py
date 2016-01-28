class Solution(object):
    def reverseList(self, head):
        return self.reverse(head, None)

    def reverse(self, head, tail):
        if not head:
            return tail

        next = head.next
        head.next = tail
        tail = head
        return self.reverse(next, tail)