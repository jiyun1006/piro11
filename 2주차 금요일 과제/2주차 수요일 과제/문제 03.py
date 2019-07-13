import random
import copy
a=list()
for i in range(9):
    a.append(input("숫자입력"))

temp=list()
b=copy.copy(a)


def cal(temp,b):
    sum=0
    for j in range(7):
        
        
        
        temp.append(int(random.choice(b)))
        sum= sum+ int(temp[j])
        b.remove(str(temp[j]))
    if sum==100:
        for i in range(7):
            temp.sort()
            print(temp[i])
    else:
        temp=list()
        b=copy.copy(a)
        cal(temp,b)


cal(temp,b)

