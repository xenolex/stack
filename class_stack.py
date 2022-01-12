from typing import Any, NoReturn, Iterator


class Stack:
    __slots__ = ("size", "__dict__")

    def __init__(self):
        self.size = 0

    def __repr__(self) -> str:
        return f'{list(self.__dict__.values())}' if self.size else '[]'

    def __len__(self) -> int:
        return self.size

    def __iter__(self) -> Iterator:
        """Return item and delete them from stack one-by-one"""
        while self.size:
            yield self.pop()

    def top(self) -> Any:
        """Return top item of the stack"""
        return self.__dict__[f'{self.size - 1}'] if self.size else None

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
        return not self.size
