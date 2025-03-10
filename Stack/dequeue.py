from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
class double_ended_queue:
    def __init__(self):
        self.q=[]
        self.front=0
        self.size=10

    def insertFront(self,data):
        if len(self.q)>=self.size:
            return -1
        self.q.insert(0,data)

    def insertRear(self,data):
        if len(self.q)>=self.size:
            return -1
        self.q.append(data)

    def deleteFront(self):
        if len(self.q)==0:
            return -1
        value=self.q.pop(0)
        return value

    def deleteRear(self):
        if not self.q :
            return -1
        value=self.q.pop()
        return value

    def getFront(self):
        if not self.q :
            return -1
        return self.q[0]
        
    def getRear(self):
        if not self.q :
            return -1
        return self.q[-1]
    
li=[int(i) for i in input().split()]
n=li[:-1]
i=0
q=double_ended_queue()
while i < len(n):
    if n[i] == 1:
        i += 1
        if i < len(n):  # Ensure index is within range
            q.insertFront(n[i])
    elif n[i] == 2:
        i += 1
        if i < len(n):  # Ensure index is within range
            q.insertRear(n[i])
    elif n[i]==3:
        ans=q.deleteFront()
        print(ans)
    elif n[i]==4:
        ans=q.deleteRear()
        print(ans)
    elif n[i]==5:
        ans=q.getFront()
        print(ans)
    elif n[i]==6:
        ans=q.getRear()
        print(ans)
    i+=1
    

# 2 32 3 5 4 6 1 109 2 100 5 6 -1