class Solution:
    # def rotate(self, nums: list[int], k: int) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     l=len(nums)
    #     k=k%l
    #     def reverse(start,end):
    #         while start<end:
    #             nums[start],nums[end]=nums[end],nums[start]
    #             start+=1
    #             end-=1
    #     reverse(0,l-1)
    #     reverse(0,k-1)
    #     reverse(k,l-1)
    ### or 
    def rotate(self,nums:list[int],k: int)-> None:
        l=len(nums)
        k=k%l
        rotate=[0]*l
        
        for i in range(l):
            rotate[(i+k)%l]=nums[i]
        for i in range(l):
            nums[i]=rotate[i]
    
nums=[1,2,3,4,5,6,7]
k=3
obj=Solution()
obj.rotate(nums,k)
print(nums)