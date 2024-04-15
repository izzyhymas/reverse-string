import pytest
from reverse_string import reverse


# Testing our Reverse Function

@pytest.fixture
def test_reverse(a: str):
    assert reverse(a == "elloH")