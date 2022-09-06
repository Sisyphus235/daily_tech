# -*- coding: utf8 -*-


class MyQueue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int):
        self.stack_in.append(x)

    def pop(self):
        if self.empty():
            return None
        if not self.stack_out:
            for _ in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

    def peek(self):
        result = self.pop()
        self.stack_out.append(result)
        return result

    def empty(self) -> bool:
        return not (self.stack_in or self.stack_out)


if __name__ == '__main__':
    obj = MyQueue()
    assert obj.push(1) is None
    assert obj.push(2) is None
    assert obj.peek() == 1
    assert obj.pop() == 1
    assert obj.empty() is False
