class Solution(object):
	def swapPairs(self, head):
		if not head: return None

		dummy = pre = ListNode(0)
		pre.next = head

		while head and head.next:
			a, b = head, head.next
			pre.next, b.next, a.next = b, a, b.next
			pre, head = a, a.next

		return dummy.next