'''
Test function Documentation
'''
import double

def test_function():
    assert double.double_int(4) == 9
    assert double.double_string("Cat") == "catcat"

test_function()