#coding:utf-8

#Given a linked list, swap every two adjacent nodes and return its head.

#For example,
#Given 1->2->3->4, you should return the list as 2->1->4->3.

#Your algorithm should use only constant space. 
#You may not modify the values in the list, only nodes itself can be changed.

import LinkList as LL

def swapPairs(head):
	if head == 0:
		return head
	cur = head
	while cur.next:
		tmp = cur.data

		cur.data = cur.next.data
		cur.next.data = tmp

		if cur.next.next:
			cur = cur.next.next
		else:
			break

	return head




l = LL.LinkList()
h = l.initlist([])

h_swap = swapPairs(h)

while h_swap:
	print h_swap.data
	h_swap = h_swap.next