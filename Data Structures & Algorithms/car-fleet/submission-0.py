class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[pos, speed] for pos, speed in zip(position,speed)]
        stack = [] # defining empty stack to keep the length
        for pos, speed in sorted(pair)[::-1]: 
            time_req = ((target-pos)/speed)
            stack.append(time_req)
            if len(stack)>= 2 and stack[-1] <= stack[-2]: 
                stack.pop()
        return len(stack)