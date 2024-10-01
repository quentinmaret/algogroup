"""
QUENTIN MARET ALGO GROUP ASSESSMENT
OPTION 2: IMPLEMENT STACK

Series of tests on stack.py run: pytest tests.py -v.
"""
import stack
import pytest


def test_stack_01():
    """push, size, pop"""
    s = stack.IntStack()
    s.push(1)
    assert s.size == 1
    assert s.pop() == 1


def test_stack_02():
    """push, size, pop"""
    s = stack.IntStack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.size == 3
    assert s.pop() == 3


def test_stack_03():
    """push, pop, size, peek"""
    s = stack.IntStack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.pop() == 3
    assert s.size == 2
    assert s.peek() == 2


def test_stack_04():
    """empty stack pop"""
    s = stack.IntStack()
    with pytest.raises(IndexError):
        s.pop()
