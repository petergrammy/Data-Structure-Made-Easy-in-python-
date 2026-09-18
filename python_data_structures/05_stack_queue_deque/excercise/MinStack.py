
class MinStack:
    def __init__(self):
        self.stack=[]
        self.min_stack=[]

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.min_stack or value<=self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self) -> None:
        self.stack.pop()
        if not self.min_stack or self.stack[-1]<=self.min_stack[-1]:
            self.min_stack.pop()


    def top(self) -> int:
        return self.stack[-1]

    def get_min(self) -> int:
        return self.min_stack[-1]
    
S=MinStack()
S.push(1)
S.push(3)
S.push(2)
print(S.get_min())