class Solution:
    def majority_element(self,nums : list[int])->int:
        # d={}
        # l=len(nums)
        # k,count=0,0
        # for i in nums:
        #     d[i]=d.get(i,0)+1
        # for i,j in d.items():
        #     if j>l/2 and j>count:
        #         k=i
        #         count=j
        # return k
        nums.sort()
        k=nums[len(nums)//2]
        return k

nums=[2,2,1,1,1,2,2]
obj=Solution()
ele=obj.majority_element(nums)
print(ele)