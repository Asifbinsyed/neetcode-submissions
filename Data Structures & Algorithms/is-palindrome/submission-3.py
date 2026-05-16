class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = [c for c in s.lower() if c.isalnum()]

        l = 0 
        r = len(cleaned)- 1 

        while l<r: 
            if cleaned[l] != cleaned[r]: 
                return False 

            l += 1 
            r -= 1 
        return True 