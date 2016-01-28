class Solution(object):
	def partition(self, head, x):
		if not head: return None

		l1, l2 = ListNode(0), ListNode(0)
		hd1, hd2 = l1, l2

		while head:
			if head.val < x:
				l1.next = head
				l1 = l1.next
			else:
				l2.next = head
				l2 = l2.next
			head = head.next

		l1.next = hd2.next
		l2.next = None

		return hd1.next