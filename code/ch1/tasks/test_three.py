"""Test the Task data type."""

from collections import namedtuple

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)


def test_defaults():
    """Using no parameters should invoke defaults."""
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2

def test_TuPac_access():
    """Check .field functionality of namedtuple."""
    t = Task('Talked Shit', 'Tu Pac')
    assert t.summary == 'Talked Shit'
    assert t.owner == 'Tu Pac'
    assert (t.done, t.id) == (False, None)

def test_biggie_access():
    t = Task('Shot Tu Pac', 'Biggie')
    assert t.summary == 'Shot Tu Pac'
    assert t.owner == 'Biggie'
    assert (t.done, t.id) == (False, None)

