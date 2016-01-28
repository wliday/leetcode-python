class Solution(object):
	def deleteDuplicates(self, head):
		if not head: return None

		dummy = pre = ListNode(0)
		dummy.next = head
		while head and head.next:
			if head.val == head.next.val:
				pre.next, head = head.next, head.next
			else:
				pre, head = pre.next, head.next

		return dummy.next