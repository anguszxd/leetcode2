def twoSum(num, target):
    process={}
    for index in range(len(num)):
        print process
        if target-num[index] in process:
            return [process[target-num[index]]+1,index+1]
        process[num[index]]=index




num=[2,7,11,15]
tar=18

ind=twoSum(num,tar)
print ind
