class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        j=1
        l=len(nums)
        for i in range(1,l):
            if j==1 or nums[i]!=nums[j-2]:
                nums[j]=nums[i]
                j+=1
        return j
nums=[0,0,1,1,1,1,2,3,3]
obj=Solution()
k=obj.removeDuplicates(nums)
print(nums[:k])
print(k)