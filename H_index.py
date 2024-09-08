class Solution:
    def hIndex(self, citations: list[int]) -> int:
        l=len(citations)
        li=[0]*(l+1)
        for i in citations:
            if i<=l:
                li[i]=li[i]+1
            else:
                li[l]=li[l]+1
        count=0
        for i in range(l,-1,-1):
            count+=li[i]
            if count>=i:
                return i
        return 0  
        
li=[3,0,6,1,5]
obj=Solution()
h_index=obj.hIndex(li)
print(h_index)
