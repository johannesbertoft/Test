import pytest
from app import add_ints

def test1():
    assert add_ints(1, 2) == 3
