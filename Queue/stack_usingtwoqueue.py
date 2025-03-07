class queue:
    def __init__(self):
        self.q1=[]
        self.q2=[]
        self.count=0

    def push(self,ele):
        while len(self.q1)!=0:
            self.q2.append(self.q1.pop(0))
        self.q1.append(ele)
        while len(self.q2)!=0:
            self.q1.append(self.q2.pop(0))
        self.count+=1

    def pop(self):
        if len(self.q1)==0:
            return 'Empty stack'
        ele=self.q1.pop(0)
        self.count-=1
        return ele  
    
    def size(self):
        return self.count
    
    def isEmpty(self):
        return self.count==0
    
    def top(self):
        if self.count==0:
            return 'Empty stack'
        return self.q1[0]

q=queue()
q.push('a')
q.push('b')
q.push('d')
print(q.top())
q.push('g')
print(q.size())
print(q.isEmpty())
print(q.top())
while not q.isEmpty() :
    print(q.pop())
