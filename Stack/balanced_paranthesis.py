#### First Approach

# def is_balanced(string):
#     s=[]
#     for char in string:
#         if char in "[{(":
#             s.append(char)
#         elif char == ")":
#             if (not s or s[-1]!='('):
#                 return False
#             s.pop()
#         elif char == '}':
#             if (not s or s[-1]!='{'):
#                 return False
#             s.pop()
#         elif char == ']':
#             if (not s or s[-1]!='['):
#                 return False
#             s.pop()
#     if not s:
#         return True
#     return False

##Second Approach
def is_balanced(string):
    s=[]
    matched_brackets={')':'(',']':'[','}':'{'}
    for char in string:
        if char in '{[(':
            s.append(char)
        elif char in '}])':
            if not s or s[-1]!=matched_brackets[char]:
                return False
            s.pop()
    return not s
    

print(is_balanced("(ghju)"))          # True
print(is_balanced("([])"))        # True
print(is_balanced("{[()]}"))      # True
print(is_balanced("{[(])}"))      # False
print(is_balanced("{{[[(())]]}}")) # True
print(is_balanced(")("))          # False
print(is_balanced("[{]"))         # False
