#coding:utf-8

#Merge two sorted linked lists and return it as a new list. 
#The new list should be made by splicing together the nodes of the first two lists.

#基本的链表使用方法就够了，注意链表的连接情况及一些特殊情况，
#如输入空链表等
import LinkList as LL

def mergeTwoLists(list1,list2):
	if list1 == 0:
		return list2
	if list2 == 0:
		return list1

	cur1 = list1
	cur2 = list2

	if cur1.data > cur2.data:
		hnew = cur2
		cur2 = cur2.next
	else:
		hnew = cur1
		cur1 = cur1.next

	cur = hnew
	while cur1 and cur2:
		if cur1.data < cur2.data:
			cur.next = cur1
			cur1 = cur1.next
			#cur = cur.next
		else:
			cur.next = cur2
			cur2 = cur2.next
		cur = cur.next

	if cur1 == 0:
		cur.next = cur2
	else:
		cur.next = cur1

	return hnew


#使用递归的方式解决问题
#递归看着很好，在python中运行速度比上一种更慢
#但在C++和C中好像比较快
def swap(n1,n2):
	temp = LL.ListNode(0)
	temp.data = n1.data
	temp.next = n1.next

	n1.data = n2.data
	n2.data = temp.data

	n1.next = n2.next
	n2.next = temp.next

def mergeTwoLists2(l1,l2):
	if l1 == 0:
		return l2
	if l2 == 0:
		return l1 

	if (l1!=0 and l2!=0) and l1.data > l2.data:
		swap(l1,l2)
	if l1!=0:
		l1.next = mergeTwoLists2(l1.next,l2)
	return l1

L1 = LL.LinkList()
H1 = L1.initlist([2])
L2 = LL.LinkList()
H2 = L2.initlist([1])

Hnew = mergeTwoLists2(H1,H2)

while Hnew:
	print Hnew.data
	Hnew = Hnew.next

