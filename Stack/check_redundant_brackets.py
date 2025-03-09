def redundant_brackets(expression):
    stack=[]
    symbol='*/-+'
    for i in expression:
        if i==')':
            count=0
            while stack:
                value=stack.pop()
                if value in symbol:
                    count+=1
                elif value=='(':
                    break
            if count==0:
                return True
        else:
            stack.append(i)
    return False

# [] means False
string=input()
value=redundant_brackets(string)
if value:
    print("true")
else:
    print("false")