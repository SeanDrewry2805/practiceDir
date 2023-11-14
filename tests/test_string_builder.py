from lib.string_builder import *

def test_counter():
    builder = StringBuilder()
    builder.add("hello")
    result = builder.size()
    result2 = builder.output()
    assert result == 5
    assert result2 == "hello"