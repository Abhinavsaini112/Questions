class Solution:
    def canJump(self, nums: list[int]) -> bool:
        farthest=0
        # for i in range(len(nums)):
        #     if i>farthest:
        #         return False
        #     farthest=max(farthest,nums[i]+i)
        # return True
        for i in nums:
            if farthest<0:
                return False
            elif i>farthest:
                farthest=i
            farthest-=1
        return True 

nums=[3,2,1,0,4]      
obj=Solution()
bool=obj.canJump(nums)
print(bool)