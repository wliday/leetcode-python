class Solution(object):
    def isPalindrome(self, head):
    	tail = None
    	slow = fast = head
    	while fast and fast.next:
    		fast = fast.next.next
    		slow, tail, tail.next= slow.next, slow, tail

    	if fast:
    		slow = slow.next

    	while tail and tail.val == slow.val:
    		tail, slow = tail.next, slow.next

    	return not tail