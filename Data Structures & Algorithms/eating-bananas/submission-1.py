class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1

        while l<r: 
            mid = l + (r-l)//2
            # calculate the speed 
            hours = 0 
            for pile in piles: 
                hours += math.ceil(pile/mid)

            if hours <= h: 
                r = mid

            elif hours > h : 
                l = mid + 1 

        return l 
            


        