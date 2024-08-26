class Solution:
    def jump(self,nums:list[int])->int:
        n=len(nums)
        if n<=1:
            return 0
        current_end,jumps,farthest=0,0,0
        for i in range(n):
            farthest=max(farthest,i+nums[i])
            if i==current_end:
                current_end=farthest
                jumps+=1
                if farthest>=n-1:
                    return jumps

        jumps
obj=Solution()
nums=[2,3,1,1,4]
x=obj.jump(nums)
print(x)
