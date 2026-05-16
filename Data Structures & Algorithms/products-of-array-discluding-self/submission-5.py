class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        left = [1] * n
        right = [1] * n
        
        # build left array
        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]
        
        # build right array
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
        
        # combine
        output = [left[i] * right[i] for i in range(n)]
        return output