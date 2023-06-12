from lib.counter import *

def test_counter_counts():
    counter1 = Counter()
    counter1.add(5)
    result1 = counter1.report()
    assert result1 == "Counted to 5 so far."
    counter2 = Counter()
    counter2.add(10)
    counter2.add(4)
    result2 = counter2.report()
    assert result2 == "Counted to 14 so far."
    
