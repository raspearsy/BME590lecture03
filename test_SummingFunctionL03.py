import pytest
import sys
import os

def testSummer():

    from SummingFunctionL03 import summer

    assert summer(2, 2) == 4
    assert summer(-1, 2) == 1
    assert summer(-1, 1) == 0
    assert summer(-4, 1) == 0

    assert summer(2.5, 2) == 4.5
    assert summer(-4.5, 2) == 0

    assert summer(complex(4, 6), 4) == complex(8, 6)
    assert summer(complex(-4, 6), 3) == 0

    assert summer('thisShouldFail', 4) == -1
    assert summer(4, 'thisShouldAlsoFail') == -1
    assert summer('this', 'fails') == -1