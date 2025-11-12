import pytest
import funcartur
def test_funcartur2():
    assert funcartur.artur (3,4) == "NO"
    assert funcartur.artur (22,20) == "YES"
    assert funcartur.artur (22,20) == "YES2"
    assert funcartur.artur (12,20) == "NO"
    assert funcartur.artur (4,8) == "NO"
