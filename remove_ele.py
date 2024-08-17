class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k=0
        l=len(nums)
        for i in range(l):
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1
        return k 

nums=[0,1,2,2,3,0,4,2]
val=2
sol=Solution()
result=sol.removeElement(nums,val)
print(result,end=' ->')
print(nums[:result])