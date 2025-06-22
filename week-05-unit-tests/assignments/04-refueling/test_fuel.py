import pytest
from fuel import convert, gauge


def test_convert_missing_slash():
    with pytest.raises(ValueError):
        convert("0.75")
    with pytest.raises(ValueError):
        convert("35")
    with pytest.raises(ValueError):
        convert("abc")


def test_convert_int_check():
    with pytest.raises(ValueError):
        convert("2.5 / 5")
    with pytest.raises(ValueError):
        convert("8 / 12.5")
    with pytest.raises(ValueError):
        convert("1.8 / 5.4")
    with pytest.raises(ValueError):
        convert("cat / 5")
    with pytest.raises(ValueError):
        convert("8 / dog")
    with pytest.raises(ValueError):
        convert("confused / rhino")


def test_convert_larger_numerator():
    with pytest.raises(ValueError):
        convert("5 / 2")
    with pytest.raises(ValueError):
        convert("15 / 3")


def test_convert_zero_denominator():
    with pytest.raises(ZeroDivisionError):
        convert("3 / 0")
    with pytest.raises(ZeroDivisionError):
        convert("12 / 0")
    with pytest.raises(ZeroDivisionError):
        convert("0 / 0")


def test_convert_valid_input():
    assert convert("0/8") == 0  # 0
    assert convert("14 / 5000") == 0  # 0.28
    assert convert("3/15") == 20  # 20
    assert convert("4 / 15") == 27  # 26.66 (round up)
    assert convert("14 / 15") == 93  # 93.33 (round down)
    assert convert("4975 / 5000") == 100  # 99.5
    assert convert("25 / 25") == 100  # 100


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(23) == "23%"
    assert gauge(77) == "77%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
