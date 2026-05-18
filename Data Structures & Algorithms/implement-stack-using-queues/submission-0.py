class MyStack:

    def __init__(self):
        self.q = deque() 
        

    def push(self, x: int) -> None:
        return self.q.append(x)

    def pop(self) -> int:
        # this si the most interestign part. 
        # first we need to pop the leftest item 
        for value in range(len(self.q) -1 ): 
            self.push(self.q.popleft())
        return self.q.popleft() 
        

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q)== 0 
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()