from lib.gratitudes import *
def test_gratitudes_list():
    gratitude1 = Gratitudes()
    gratitude1.add("Health")
    gratitude1.add("Wealth")
    assert gratitude1.format() == "Be grateful for: Health, Wealth"