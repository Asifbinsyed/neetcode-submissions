class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for i in range(len(nums)):
            discount = target - nums[i]
            dict1[discount] = i
        for i,num in enumerate(nums): 
            if num in dict1.keys() and i != dict1[num]: 
                return sorted([i,dict1[num]])