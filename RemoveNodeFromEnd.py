#coding:utf-8

#Remove Nth Node From End of List 
#Given a linked list, remove the nth node from the end of list and return its head.

#一次遍历完成：先找到两个node，第一个node和第n个node，
#两个node同时前进，当后面一个node到List最末位时，
#前一个node所在的位置是倒数第n个node，将其删除就可以了
import LinkList as LL

def removeNthFromEnd(head,n):
	curNode = head
	NthNode = head
	for i in range(0,n-1):
		NthNode = NthNode.next
	print NthNode.data

	if NthNode.next == 0:
		return curNode.next

	while NthNode.next:
		preNode = curNode
		curNode = curNode.next
		NthNode = NthNode.next

	preNode.next = curNode.next
	return head


l = LL.LinkList()
h = l.initlist([1])
h_moved = removeNthFromEnd(h,1)
#while h:
#	print h.data
#	h = h.next

while h_moved:
	print h_moved.data
	h_moved = h_moved.next