class Stack:
    def __init__(self):
        self.st = []

    def push(self, elem):
        self.st.append(elem)

    def popS(self):
        return self.st.pop()

    def peek(self):
        return self.st[-1]

    def __str__(self):
        return "[" + ", ".join(str(i) for i in self.st) + "]"
