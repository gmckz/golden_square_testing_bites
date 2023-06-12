from lib.check_codeword import *

def test_check_codeword_grant_access():
    
    assert check_codeword("horse") == "Correct! Come in."
    assert check_codeword("hose") == "Close, but nope."
    assert check_codeword("wrong") == "WRONG!"
    
