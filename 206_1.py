class Solution(object):
    def reverseList(self, head):

    	tail = None
    	while head:
    		next = head.next
    		tail, head.next = head, tail
    		head = next

    	return tail