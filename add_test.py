import pytest
from app import add_ints


def test_add():
    assert add_ints(1, 2) == 3


