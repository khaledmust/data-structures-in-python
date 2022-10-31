class Stack:
    # Create the stack.
    def __init__(self):
        self._elements = []

    # Adds an element to the top of the stack.
    def push(self, element):
        self._elements.append(element)

    # Removes and returns the top-most element of the stack.
    def pop(self):
        return self._elements.pop()

    # Returns the size of the stack.
    def size(self):
        return len(self._elements)

    # Returns the top-most element of the stack.
    def peek(self):
        tmp = self._elements.pop(-1)
        self._elements.append(tmp)
        return tmp

    # Returns the state of the stack.
    def is_empty(self):
        return len(self._elements) == 0
