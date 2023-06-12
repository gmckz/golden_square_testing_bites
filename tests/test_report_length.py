from lib.report_length import *
def test_report_length_return_len_of_string():
    assert report_length("Hello World!") == "This string was 12 characters long."
    assert report_length("Gemma") == "This string was 5 characters long."
    assert report_length("a")== "This string was 1 characters long."