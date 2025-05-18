class queue:
    def __init__(self):
        self._stack_in = [] 
        self._stack_out = [] 
        self.__size = 10
        self.__count = 0

    def enqueue(self, x):
        if self.__count < self.__size:
            self._stack_in.append(x)
            self.__count += 1 

        else:
            print("Queue overflow")

    def dequeue(self):
        if not self._stack_in and not self._stack_out:
            print("Queue underflow")
            return 

        if not self._stack_out:
            while self._stack_in:
                self._stack_out.append(self._stack_in.pop())

        self.__count -= 1 
        
        return self._stack_out.pop()
    
    def top(self):
        if not self._stack_in and not self._stack_out:
            print("Queue is empty")
            return

        if not self._stack_out:
            while self._stack_in:
                self._stack_out.append(self._stack_in.pop())
        
        return self._stack_out[-1]

    def print_queue(self):
        if not self._stack_in and not self._stack_out:
            print("Queue is empty")
        elif not self._stack_in:
            print(self._stack_out)
        else:
            print(self._stack_in)


q = queue()
for i in range(1, 10):
    q.enqueue(i)
q.print_queue()
q.dequeue()
q.print_queue()
q.enqueue(11)
q.enqueue(13)
q.print_queue()