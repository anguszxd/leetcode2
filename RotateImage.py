#coding:utf-8

#You are given an n x n 2D matrix representing an image.

#Rotate the image by 90 degrees (clockwise).

#Follow up:
#Could you do this in-place?
import copy

#Solution1:旋转就是挪动元素位置，每次挪动时，4个相关位置会轮换，
#只要找到这4个位置的关系就可以了。其次，每次挪动只与当前所在圈有关，
#因此可以写出一圈上转动的函数，在用循环的方式，逐渐向内圈移动
def rotate(image):
	tmpimage = copy.deepcopy(image)

	n = len(image[0])
	for start in range(n/2):
		helper(image, tmpimage, start)
	return image

def helper(image, tmpimage, start):
	n = len(tmpimage[0])
	for i in range(start,n-1-start):
		image[start][i] = tmpimage[n-1-i][start]
		image[i][n-1-start] = tmpimage[start][i]
		image[n-start-1][n-1-i] = tmpimage[i][n-1-start]
		image[n-1-i][start] = tmpimage[n-start-1][n-1-i]


def helper2(image):
	n = len(image[0])
	tmpimage = copy.deepcopy(image)
	for i in range(n-1):
		tmp = [tmpimage[0][i],tmpimage[i][n-1],tmpimage[n-1][n-1-i],tmpimage[n-1-i][0]]
		image[0][i] = tmp[3]
		image[i][n-1] = tmp[0]
		image[n-1][n-i-1] = tmp[1]
		image[n-1-i][0] = tmp[2]
	return image

image = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
#image = [[1,2],[3,4]]
print image
print rotate(image)