from funcShavkatov import shavkatov

def test_equal():
    assert shavkatov(5, 5) == "Yes"
    assert shavkatov(0, 0) == "Yes"
    assert shavkatov(-10, -10) == "Yes"

def test_not_equal():
    assert shavkatov(5, 6) == "no"
    assert shavkatov(1, 2) == "no"
    assert shavkatov(3.5, 4.5) == "no"