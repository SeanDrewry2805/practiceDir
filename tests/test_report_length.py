from lib.report_length import *

def test_add_five_returns_eight_for_three():
    result1 = report_length("horse")
    length1 = len("horse")
    result2 = report_length("hose")
    length2 = len("hose")
    result3 = report_length("Ponpon")
    length3 = len("Ponpon")
    assert result1 == f"This string was {length1} characters long."
    assert result2 == f"This string was {length2} characters long."
    assert result3 == f"This string was {length3} characters long."