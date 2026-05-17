class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # this is stack problem 
        stacks = [] 
        for ops in operations: 
            if ops == "+": 
                stacks.append(stacks[-1] + stacks[-2])

            elif ops == "D":
                stacks.append(2* stacks[-1]) 

            elif ops == "C": 
                stacks.pop()

            else: 
                stacks.append(int(ops))

        return sum(stacks)

        