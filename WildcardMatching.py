#coding:utf-8

#'?' Matches any single character.
#'*' Matches any sequence of characters (including the empty sequence).

#The matching should cover the entire input string (not partial).

#The function prototype should be:
#bool isMatch(const char *s, const char *p)

#Some examples:
#isMatch("aa","a") → false
#isMatch("aa","aa") → true
#isMatch("aaa","aa") → false
#isMatch("aa", "*") → true
#isMatch("aa", "a*") → true
#isMatch("ab", "?*") → true
#isMatch("aab", "c*a*b") → false

def isMatch(s,p):


s = "aab"
p = "c*a*b"