"""
Test src.tool.py
"""

import pytest

from src.tool import func


@pytest.mark.parametrize("arg1, arg2, expected", [
    (2, 3, True),
    (-1, 1, True),
    (0, 0, True),
])
def testFunc(arg1, arg2, expected):
    assert func(arg1, arg2) == expected
