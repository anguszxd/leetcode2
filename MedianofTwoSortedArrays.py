def findKth(num1,num2,k):
	m = len(num1)
	n = len(num2)
	if m > n:
		return findKth(num2,num1,k)
	if m == 0:
		return num2[k-1]
	if k == 1:
		return min(num1[0],num2[0])

	pa = min(k/2,m)
	pb = k - pa
	if num1[pa-1] < num2[pb-1]:
		return findKth(num1[pa:],num2,k-pa)
	elif num1[pa-1] > num2[pb-1]:
		return findKth(num1,num2[pb:],k-pb)
	else:
		return num1[pa-1]

def findMedianSortedArrays(num1,num2):
	m = len(num1)
	n = len(num2)
	total = m+n
	if total & 0x1:
		return findKth(num1,num2,total/2+1)
	else:
		return (float(findKth(num1,num2,total/2))+float(findKth(num1,num2,total/2+1)))/2
		#return (float(a)+float(b))/2


#num1=[1,4,5,6,8,10,14]
#num2=[2,5,6,9,11,13,17,19,22]
num1=[1,2]
num2=[1,2]
med = findMedianSortedArrays(num1,num2)
print med