from lib.greet import *

def test_add_five_returns_eight_for_three():
    result = greet("sean")
    assert result == f"Hello, sean!"