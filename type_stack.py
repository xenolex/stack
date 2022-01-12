"""stack based on type is about 1 second faster on push with 10_000_000 operations than class based"""

from typing import Any, NoReturn


def _init(self):
    self.size = 0


def _iter(self):
    while self.size:
        yield self.pop()


def _push(self, item) -> NoReturn:
    self.__dict__[f'{self.size}'] = item
    self.size += 1


def _pop(self) -> Any:
    self.size -= 1
    if self.size > -1:
        item_name = f'{self.size}'
        item = self.__dict__[item_name]
        del self.__dict__[item_name]
    else:
        self.size = 0
        raise IndexError('pop from empty Stack')
    return item


def _clear(self) -> NoReturn:
    self.size = 0
    self.__dict__.clear()


stack = type('stack', (), {
    "__slots__": ("size", "__dict__"),
    "__init__": _init,
    "__repr__": lambda self: f'{list(self.__dict__.values())}' if self.size else '[]',
    "__len__": lambda self: self.size,
    "__iter__": _iter,  # Return item and delete them from stack one-by-one
    "top": lambda self: self.__dict__[f'{self.size - 1}'] if self.size else None,  # Return top item of the stack
    "push": _push,  # Add item on top of the stack
    "pop": _pop,  # Return top item and delete it from stack
    "clear": _clear,  # Delete all items from stack
    "is_empty": lambda self: not self.size  # Return True if stack is empty
}
             )
