class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = []
        for i in range(len(nums)):
            out = 1
            for j in range(len(nums)):
                if i != j:
                    out *= nums[j]
            results.append(out)
        return results