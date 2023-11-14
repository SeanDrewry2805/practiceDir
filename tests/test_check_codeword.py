from lib.check_codeword import *

def test_add_five_returns_eight_for_three():
    result1 = check_codeword("horse")
    result2 = check_codeword("hose")
    result3 = check_codeword("Pony")
    assert result1 == "Correct! Come in."
    assert result2 == "Close, but nope."
    assert result3 == "WRONG!"