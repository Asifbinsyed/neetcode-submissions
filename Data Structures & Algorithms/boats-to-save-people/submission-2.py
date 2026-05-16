class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l , r = 0 , len(people)- 1 
        boat_cnt = 0  
        while l <=  r :
            if l == r: 
                boat_cnt += 1
                break 
            tot_wt = people[l] + people[r]
            if tot_wt > limit: 
                r -= 1
                boat_cnt += 1  
            else: 
                boat_cnt += 1 
                l += 1 
                r -= 1 

        return boat_cnt 

        