class Solution(object):
	def removeNthFromEnd(self, head, n):
		if not head: return None

		dummy = ListNode(0)
		dummy.next = head
		slow = fast = dummy

		for x in range(n + 1):
			fast = fast.next

		while fast:
			slow, fast = slow.next, fast.next

		slow.next = slow.next.next

		return dummy.next