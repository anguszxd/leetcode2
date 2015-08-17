#coding:utf-8

#Given a string containing just the characters '(' and ')', find the length of the longest valid 
#(well-formed) parentheses substring.

#For "(()", the longest valid parentheses substring is "()", which has length = 2.

#Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

#分析：括号配对是进栈出栈问题，即左括号视为进栈，右括号视为出栈，
#括号匹配错误即栈空时还要出栈
#进栈出栈的操作也可以用加减代替，比如进栈即来了左括号，+1，
#出栈即来了右括号，-1；用left这个变量表示当前栈中元素数量（左括号数量）
#这个问题就变成了，找到最长的子串，这个子串遍历一遍可以使得left=0（left初始值为0）
#子串不满足条件，即left<0
def longestValid(s):
	longest, curlen, left, last = 0, 0, 0, 0
	if s == "":
		return longest
	for i in range(len(s)):
		if s[i] == "(":
			left += 1
		else:
			left -= 1
		if left < 0:
			longest = max(longest, last)
			curlen = 0
			left = 0
			last = 0
		elif left == 0:
			last += curlen
		else:
			curlen += 1
		print last
	#if left == 0:
	longest = max(longest, curlen-left)


	return longest


#前面的分析不够全面，不能涵盖全部情况
#用stack保存前面累积的正确匹配的长度
def longestValidParentheses(s):
    stack, longest, index = [0], 0, 0

    for index in xrange(0, len(s)):
        if s[index] == ")" and len(stack) != 1:
            length, last = stack.pop(), stack.pop()
            total_length = last + length + 2
            stack.append(total_length)
            longest = max(longest, total_length)
        elif s[index] == "(":
            stack.append(0)
        else:
            stack = [0]

    return longest


s = ")("

#print longestValidParentheses(s)
print longestValidParentheses(s)