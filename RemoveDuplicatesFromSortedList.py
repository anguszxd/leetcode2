#coding:utf-8

#Given a sorted linked list, delete all duplicates such that each element appear only once.

#For example,
#Given 1->1->2, return 1->2.
#Given 1->1->2->3->3, return 1->2->3.

import LinkList as LL

#Solution:变量tmp用于储存当前data的node，如果下一个节点的
#data和cur.data相同，那么tmp内容不变，继续遍历链表；
#若cur.data != cur.next.data，说明内容发生了变换，
#则要用tmp.next连接cur.next，并用cur.next更新tmp；
#最后一个tmp注意和后面的节点断开，即加上tmp.next = 0
def deleteDuplicates(head):
	#newhead = head
	if head == 0 or head.next == 0:
		return head
	cur = head
	tmp = head
	while cur.next:
		if cur.data != cur.next.data:
			tmp.next = cur.next
			tmp = cur.next
		cur = cur.next

	tmp.next = 0

	return head

l = LL.LinkList()
h = l.initlist([1,1])

h_remove = deleteDuplicates(h)

while h_remove:
	print h_remove.data
	h_remove = h_remove.next