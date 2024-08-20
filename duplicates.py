class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l=len(nums)
        if l==0:
            return 0
        elif l==1:
            return 1
        j=0
        # i=0
        # while i<l:
        #     if nums[i]!=nums[j]:
        #         j+=1
        #         nums[j]=nums[i]
        #     i+=1
        # return j+1
        for i in range(l):
            if nums[i]!=nums[j]:
                j+=1
                nums[j]=nums[i]

        return j+1


nums=[0,0,1,1,1,2,2,3,3,4]
k=2
obj=Solution()
k=obj.removeDuplicates(nums)
print(k)
print(nums[:k])