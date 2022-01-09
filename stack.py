from typing import Any, NoReturn, Iterator


class Stack:
    __slots__ = "__dict__", "size"

    def __init__(self):
        self.size = 0

    def __repr__(self) -> str:
        return f'{list(self.__dict__.values())}' if self.size else '[]'

    def __len__(self):
        return self.size

    def __iter__(self) -> Iterator:
        """Return item and delete them from stack one-by-one"""
        while self.size:
            yield self.pop()

    def top(self) -> Any:
        """Return top item of the stack"""
        if self.size:
            return self.__dict__[f'{self.size - 1}']
        else:
            return ''

    def push(self, item) -> NoReturn:
        """Add item on top of the stack"""
        self.__dict__[f'{self.size}'] = item
        self.size += 1

    def pop(self) -> Any:
        """Return top item and delete it from stack"""
        self.size -= 1
        if self.size > -1:
            item_name = f'{self.size}'
            item = self.__dict__[item_name]
            del self.__dict__[item_name]
        else:
            self.size = 0
            raise IndexError('pop from empty Stack')
        return item

    def clear(self) -> NoReturn:
        """Delete all items from stack"""
        self.size = 0
        self.__dict__.clear()

    def is_empty(self) -> bool:
        """Return True if stack is empty"""
        return True if not self.size else False


def _init(self):
    self.size = 0


def _repr(self):
    return f'{list(self.__dict__.values())}' if self.size else '[]'


def _len(self):
    return self.size


def _push(self, item):
    self.__dict__[f'{self.size}'] = item
    self.size += 1


def _pop(self) -> Any:
    """Return top item and delete it from stack"""
    self.size -= 1
    if self.size > -1:
        item_name = f'{self.size}'
        item = self.__dict__[item_name]
        del self.__dict__[item_name]
    else:
        self.size = 0
        raise IndexError('pop from empty Stack')
    return item


stack = type('stack', (), {"__slots__": ("size", "__dict__"),
                           "__init__": _init,
                           "__repr__": _repr,
                           "__len__": _len,
                           "push": _push,
                           "pop": _pop}
             )

if __name__ == '__main__':
    a = Stack()
    a.push(1)
    b = stack()
    b.push(1)
    setup = """
from stack import stack,Stack
b = Stack()
a = stack()
for i in range(10000000):
    a.push(i)
    b.push(i)
    """
