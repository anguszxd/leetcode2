#-*- coding: UTF-8 -*-
#八皇后问题的python解决
#冲突函数， 冲突返回true
def conflict(state,nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i]-nextX) in (0,nextY-i): #只要有一个冲突的，就返回冲突
            return True
    return False                               #如果都不冲突，则返回不冲突
#num 是皇后的总数，state是存放前面皇后位置信息的元组:递归代码简化版         
def queen(num=8,state=()):                     #state从空开始递增，第一个为(0,)..
    for pos in range(num):
        if not conflict(state,pos):
            if len(state)==num-1:
                yield((pos,))
            else:
                for result in queen(num,state+(pos,)):
                    yield((pos,)+result)
for solution in queen(8):
    print(solution)