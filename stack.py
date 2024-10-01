"""
QUENTIN MARET ALGO GROUP ASSESSMENT
OPTION 2: IMPLEMENT STACK

Referring to the linked Wikipedia page, I have decided
to implement the stack as a singly linked list.
(https://en.wikipedia.org/wiki/Stack_(abstract_data_type)
"""
from abc import ABC, abstractmethod
from typing import Optional


class Stack(ABC):
    """
    Abstract base class for the stack.
    """
    @abstractmethod
    def push(self, data: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def pop(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def peek(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def size(self) -> int:
        raise NotImplementedError

    @property
    @abstractmethod
    def show(self):
        raise NotImplementedError


class IntNode:
    """
    Class for singly linked list node.
    """
    def __init__(self, data: Optional[int] = None) -> None:
        self.data = data
        self.next: Optional[IntNode] = None


class IntStack(Stack):
    """
    Class for singly linked list integer stack.
    """
    def __init__(self):
        self.head: IntNode = IntNode()
        self.size: int = 0

    def push(self, data: int) -> None:
        self.size += 1
        node = IntNode(data)
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = node

    def pop(self) -> int:
        if self.size == 0:
            raise IndexError('Stack is empty')
        self.size -= 1
        curr = self.head
        while curr.next.next is not None:
            curr = curr.next
        data = curr.next.data
        curr.next = None
        return data

    def peek(self):
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        return curr.data

    def size(self) -> int:
        return self.size

    @property
    def show(self):
        print(f'size: {self.size}\n')
        curr = self.head
        while curr.next is not None:
            curr = curr.next
            print(f'data: {curr.data}')
