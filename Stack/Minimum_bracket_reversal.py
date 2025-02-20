def minimum_bracket_reversal(string):
    if len(string)%2!=0:
        return -1
    stack=[]
    for i in string:
        if i =='{':
            stack.append(i)
        elif (i=='}' and not stack ) or (i=='}' and stack[-1]=='}'):
            stack.append(i)
        elif i=='}':
            stack.pop()
    count=0
    while stack:
        c1=stack.pop()
        c2=stack.pop()
        if c1!=c2:
            count+=2
        else:
            count+=1
    return count

print(minimum_bracket_reversal("{{{{}}"))  # Output: 1
print(minimum_bracket_reversal("}{{}}{{{"))  # Output: 3