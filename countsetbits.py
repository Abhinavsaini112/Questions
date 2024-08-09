def largestPower2(n):
    x=0
    while 2**x<=n:
        x+=1
    return x-1

def count_bits(n):
    if n==0:
        return 0
    x=largestPower2(n)
    btill2x=(2**(x-1))*x
    add=n-(2**x)+1
    rest=(n-2**x)
    total_bits=btill2x+add+count_bits(rest)
    return total_bits

n=int(input('Enter the positive interger value :'))
print(count_bits(n))
    