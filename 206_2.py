class Solution(object):
    def reverseList(self, head):
        return self.reserve(head, None)
        
    def reserve(self, head, tail):
        if not head: return tail
        next = head.next
        head.next = tail
        return self.reserve(next, head)