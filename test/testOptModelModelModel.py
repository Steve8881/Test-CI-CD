"""
Test src.optModel.model.model.py
"""

import pytest

from src.optModel.model.model import addNumbers, mulNumbers
import src.optModel.model.model


def testAddNumbers(mocker):
    mockMulNumbers = mocker.patch("src.optModel.model.model.mulNumbers")
    mockMulNumbers.return_value = 1
    assert src.optModel.model.model.mulNumbers(1, 2) == 1
    assert mulNumbers(1, 2) == 2

    assert addNumbers(1, 2) == 3

    with pytest.raises(TypeError, match="Both arguments must be numbers."):
        addNumbers("a", 2)

    with pytest.raises(TypeError, match="Both arguments must be numbers."):
        mulNumbers("a", 2)
