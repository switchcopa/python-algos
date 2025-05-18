class Stack:
    def __init__(self, size=100):
        self._stack = []
        self.size = size
        self.count = 0

    def push(self, x):
        if self.size > self.count:
            self._stack.append(x)
            self.count += 1 

            return True 
        else:
            print("Stack overflow")

    def pop(self):
        if self._stack:
            self.count -= 1
            return self._stack.pop()
        else:
            print("Stack underflow")
        
    def peek(self):
        if self._stack:
            return self._stack[-1]
        else:
            print("peek from empty stack")

    def print_stack(self):
        print(self._stack)
    
s = Stack(5)
s.push(3)
s.push(7)
s.push(2)
s.print_stack()
e = s.pop()
print("Popped element:", e)
s.print_stack()
s.push(11)
s.push(17)
s.print_stack()
s.push(13)
s.print_stack()
s.push(23)