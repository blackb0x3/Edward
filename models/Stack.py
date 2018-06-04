class Stack:
    def __init__(self):
        self._stack_vals = []
        self.pointer = 0

    def push(self, *args):
        for arg in args:
            self._stack_vals[self.pointer] = arg
            self.pointer += 1

    def pop(self):
        popped_val = self._stack_vals.pop(self.pointer)
        self.pointer -= 1
        return popped_val