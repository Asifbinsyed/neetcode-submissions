class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic1 = {}
        for num in nums: 
            dic1[num] = dic1.get(num,0) + 1 

        buckets = [ [] for _ in range(len(nums)+1)]
        for num,freq in dic1.items(): 
            buckets[freq].append(num) 

        results = []
        for i in range(len(nums),0,-1): 
            for j in buckets[i]: 
                results.append(j)
                if len(results) == k: 
                    return results
                
            

            


        