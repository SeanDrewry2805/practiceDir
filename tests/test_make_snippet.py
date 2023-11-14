from lib.make_snippet import *

def test_make_snippet_5_words():
    result = make_snippet("hello my name is sean")
    assert result == "hello my name is sean"

def test_make_snippet_6_words():
    result = make_snippet("hello my name is sean drewry")
    assert result == "hello my name is sean..."