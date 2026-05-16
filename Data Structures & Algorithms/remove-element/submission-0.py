class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
            low_index = 0
            for num in nums:
                if num != val:
                    nums[low_index] = num
                    low_index += 1
            return low_index