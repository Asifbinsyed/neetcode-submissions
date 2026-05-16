class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        # TODO: implement (not in-place). Return a new list.
        if len(nums) <=1: 
            return list(nums)

        mid = len(nums)//2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self.merge(left, right)

    def merge(self,left, right): 
        out = [] 
        i,j = 0, 0
        while i<len(left) and j< len(right): 
            if left[i] <= right[j]: 
                out.append(left[i])
                i += 1 

            else:
                out.append(right[j])
                j += 1 

        out.extend(left[i:])
        out.extend(right[j:])

        return out 


        