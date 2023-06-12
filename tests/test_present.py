import pytest
from lib.present import *

def test_present_wraps_exception():
    present = Present()
    present.wrap("abc")
    with pytest.raises(Exception) as e:
        present.wrap("123")
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."
    
def test_present_unwrap_exception():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."
    
def test_unwrap_contents():
    present = Present()
    present.wrap("123")
    assert present.unwrap() == "123"


def test_wrapping_already_wrapped():
    present = Present()
    present.wrap("abc")
    with pytest.raises(Exception) as e:
        present.wrap("123")
    assert present.unwrap() == "abc"