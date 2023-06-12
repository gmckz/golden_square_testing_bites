#import the function to test
from lib.add_five import *

#create single test example
#function name must start with "test_" for pytest to find it
#rest of function describes what the test verifies
def test_add_five_returns_eight_for_three():
    result = add_five(3) #run func with example argument 3
    assert result == 8 #assert that in this example it should return 8 