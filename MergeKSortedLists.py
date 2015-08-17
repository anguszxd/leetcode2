#coding:utf-8
#Merge k sorted linked lists and return it as one sorted list.
#Analyze and describe its complexity.

import LinkList as LL

#采用分而治之的方法，先将所有链表不断分成两组，知道每组只剩两个链表或更少
#再两两组成新链表，最终将所有链表融合在一起
#可以参考LongestCommonPrefix中分而治之的方法
#用分而治之的方法再加上原有的两个排序链表融合
#很容易就能得到K个链表融合
#mergeTwoLists也可以用另一种方法，而且速度更快些，
#在leetcode中AC的代码用的就是另一种直接融合的方法
def mergeKLists(lists):
	if not lists:
		return 0
	if len(lists) == 1:
		return lists[0]

	h1 = mergeKLists(lists[:len(lists)//2])
	h2 = mergeKLists(lists[len(lists)//2:])

	return mergeTwoLists(h1,h2)

def swap(n1,n2):
	temp = LL.ListNode(0)
	temp.data = n1.data
	temp.next = n1.next

	n1.data = n2.data
	n2.data = temp.data

	n1.next = n2.next
	n2.next = temp.next

def mergeTwoLists(l1,l2):
	if l1 == 0:
		return l2
	if l2 == 0:
		return l1 

	if (l1!=0 and l2!=0) and l1.data > l2.data:
		swap(l1,l2)
	if l1!=0:
		l1.next = mergeTwoLists(l1.next,l2)
	return l1

	
L1 = LL.LinkList()
H1 = L1.initlist([])
L2 = LL.LinkList(
H2 = L2.initlist([])
L3 = LL.LinkList()
H3 = L3.initlist([])

ls = [H1,H2,H3]

Hnew = mergeKLists([])

while Hnew:
	print Hnew.data
	Hnew = Hnew.next
