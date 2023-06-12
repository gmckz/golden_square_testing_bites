import pytest
from lib.password_checker import *

def test_password_long_enough():
    password = PasswordChecker()
    assert password.check("12345678")== True
def test_password_not_long_enough():
    password = PasswordChecker()
    with pytest.raises(Exception) as e:
        password.check('1234')
    error_message = str(e.value)
    assert error_message=="Invalid password, must be 8+ characters."
