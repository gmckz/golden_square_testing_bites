from lib.string_builder import *

def test_string_builder():
    string1 = StringBuilder()
    string1.add("Hello")
    assert string1.size() == 5
    assert string1.output() == "Hello"
    string2 = StringBuilder()
    string2.add("Hi ")
    string2.add("Navin!")
    assert string2.size() == 9
    assert string2.output() == "Hi Navin!"
