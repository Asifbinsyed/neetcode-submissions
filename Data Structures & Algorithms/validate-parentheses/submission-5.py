class Solution:
    def isValid(self, s: str) -> bool:
        stacks = [] 
        ClosetoOpen = { ")": "(", 
        "}": "{", 
        "]" : "["}
        for c in s : 
            if c in ClosetoOpen: 
                if stacks and ClosetoOpen[c]==stacks[-1]:
                    stacks.pop()
                else: 
                    return False
            else: 
                    stacks.append(c)

        return True if not stacks else False 
            