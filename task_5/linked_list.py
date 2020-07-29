import reprlib
from typing import Optional, NoReturn, List

from task_5.node import Node


class LinkedList:
    def __init__(self,
                 nodes: Optional[List[Node]] = None,
                 head_node: Optional['Node'] = None,
                 tail_node: Optional['Node'] = None):
        if head_node or tail_node:
            self._head = head_node
            self._tail = head_node
        elif tail_node:
            self._head = tail_node
            self._tail = tail_node
        else:
            self._head = nodes[0]
            self._tail = self._head
            for node in nodes[1:]:
                self.add_to_tail(node)

    def __repr__(self) -> str:
        llist_string = reprlib.repr([node for node in self])
        return llist_string

    __str__ = __repr__

    def __iter__(self) -> Node:
        current_node = self._head
        while current_node is not None:
            yield current_node
            current_node = current_node.next

        return

    def __contains__(self, node: Node) -> bool:
        return self.contain(node)

    def add_to_tail(self, node: Node) -> NoReturn:
        self._tail.next = node
        node.prev = self._tail
        self._tail = node

    def add_to_head(self, node: Node) -> NoReturn:
        self._head.prev = node
        node.next = self._head
        self._head = node

    def contain(self, checked_node: Node) -> bool:
        for node in self:
            if node == checked_node:
                return True

        return False

    def remove(self, removed_node: Node) -> bool:
        """
        This method removes the first met node.
        :param removed_node: a node for deleting.
        :return: True is a node was found and deleted and False otherwise.
        """

        if removed_node == self._head:
            self._head = self._head.next
            self._head.prev = None
        elif removed_node == self._tail:
            self._tail = self._tail.prev
            self._tail.next = None
        else:
            for node in self:
                if node == removed_node:
                    prev_node = node.prev
                    next_node = node.next
                    prev_node.next, next_node.prev = next_node, prev_node
                    return True

        return False

    def reverse(self) -> NoReturn:
        """
        This method reverses a linked list.
        :return:
        """

        current_node = self._tail
        self._head, self._tail = self._tail, self._head
        while current_node is not None:
            prev_node = current_node.prev
            current_node.prev = current_node.next
            current_node.next = prev_node
            current_node = prev_node
