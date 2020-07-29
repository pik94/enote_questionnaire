from typing import Optional, NoReturn, List


class Node:
    def __init__(self,
                 value: object,
                 next: Optional['Node'] = None,
                 prev: Optional['Node'] = None):
        self.value = value
        self.next = next
        self.prev = prev

    def __eq__(self, node: 'Node') -> bool:
        return self.value == node.value

    def __repr__(self):
        return f'Node(value={self.value})'

    __str__ = __repr__
