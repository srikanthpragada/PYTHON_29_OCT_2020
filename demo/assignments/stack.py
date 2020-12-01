class Stack_Iterator:
    def __init__(self, data):
        self.data = data
        self.pos = len(data) - 1

    def __next__(self):
        if self.pos < 0:
            raise StopIteration

        v = self.data[self.pos]
        self.pos -= 1
        return v


class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    @property
    def length(self):
        return len(self.data)

    def __iter__(self):
        return Stack_Iterator(self.data)


s = Stack()
s.push(10)
s.push(20)

# Use iterator to get all values from Stack
for v in s:
    print(v)

print(s.pop())
print(s.peek())
