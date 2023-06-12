from lib.greet import *

def test_greet_returns_string_with_name():
    result = greet("Navin")
    assert result == "Hello, Navin!"