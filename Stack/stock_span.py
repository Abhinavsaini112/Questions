def stock_span(li):
    n=len(li)
    span=[0]*n
    stack=[]
    for i in range(n):
        while stack and stack[-1][0]<li[i]:
            stack.pop()
        if not stack:
            span[i]=i+1
        else :
            span[i]=i-stack[-1][1]
        stack.append((li[i],i))
    return span

li=[100,80,60,70,60,75,85]
span=stock_span(li)
print(span)
