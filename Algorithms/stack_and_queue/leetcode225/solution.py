# -*- coding: utf8 -*-

class MyStack:

    def __init__(self):
        self.op = []
        self.store = []

    def push(self, x: int) -> None:
        self.op.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        if not self.op:
            while self.store:
                self.op.append(self.store.pop(0))
        while len(self.op) > 1:
            self.store.append(self.op.pop(0))
        return self.op.pop(0)

    def top(self) -> int:
        result = self.pop()
        self.op.append(result)
        return result

    def empty(self) -> bool:
        return not (self.op or self.store)


if __name__ == '__main__':
    obj = MyStack()
    assert obj.push(1) is None
    assert obj.push(2) is None
    assert obj.top() == 2
    assert obj.pop() == 2
    assert obj.empty() is False
