import pytest

from app.utils import add


@pytest.mark.parametrize("a, b, expected", [(1, 1, 2), (100, 150, 250)])
def test_add(a, b, expected):
    assert add(a, b) == expected
