from lib.gratitudes import *

def test_gratitudes():
    gratitudes = Gratitudes()
    gratitudes.add("Sean")
    result = gratitudes.format()
    assert result == "Be grateful for: Sean"
