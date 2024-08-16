from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        
        l = len(nums1) - 1  # Start from the last index of nums1
        m -= 1  # Adjust m to point to the last element of nums1's valid part
        n -= 1  # Adjust n to point to the last element of nums2
        
        # Merge the arrays from the end
        while m >= 0 and n >= 0:
            if nums1[m] >= nums2[n]:
                nums1[l] = nums1[m]
                m -= 1
            else:
                nums1[l] = nums2[n]
                n -= 1
            l -= 1
        
        # If there are any remaining elements in nums2, copy them over
        while n >= 0:
            nums1[l] = nums2[n]
            n -= 1
            l -= 1
# Example usage:
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

Solution().merge(nums1, m, nums2, n)
print(nums1)  # Output should be [1, 2, 2, 3, 5, 6]