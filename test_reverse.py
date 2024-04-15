import pytest
from reverse_string import reverse


# Testing our Reverse Function
def test_reverse():
    a = reverse("Hello")
    assert a == "olleH"