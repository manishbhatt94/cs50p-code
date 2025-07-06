import pytest
from working import convert


def test_conversion():
    assert convert("9:05 AM to 3 PM") == "09:05 to 15:00"
    assert convert("6 PM to 12:45 AM") == "18:00 to 00:45"
    assert convert("12 PM to 4 AM") == "12:00 to 04:00"
    assert convert("11:01 AM to 7:59 AM") == "11:01 to 07:59"


def test_invalid_format():
    with pytest.raises(ValueError, match="Input format is invalid"):
        convert("hello world")
    with pytest.raises(ValueError, match="Input format is invalid"):
        convert("aa:bb AM to cc:dd PM")
    with pytest.raises(ValueError, match="Input format is invalid"):
        convert("9:00 am to 5:00 pm")
    with pytest.raises(ValueError, match="Input format is invalid"):
        convert("9:00 AM - 5:00 PM")
    with pytest.raises(ValueError, match="Input format is invalid"):
        convert("9AM to 5PM")
    with pytest.raises(ValueError, match="Input format is invalid"):
        convert("9:00 AM to 5:001 PM")


def test_invalid_time():
    with pytest.raises(ValueError, match="Time is invalid"):
        convert("0:00 AM to 8:00 PM")
    with pytest.raises(ValueError, match="Time is invalid"):
        convert("7:60 AM to 8:00 PM")
    with pytest.raises(ValueError, match="Time is invalid"):
        convert("13:00 AM to 8:00 PM")
    with pytest.raises(ValueError, match="Time is invalid"):
        convert("7:00 AM to 0:00 PM")
    with pytest.raises(ValueError, match="Time is invalid"):
        convert("7:00 AM to 8:75 PM")
    with pytest.raises(ValueError, match="Time is invalid"):
        convert("7:00 AM to 14:00 PM")
    # diff format
    with pytest.raises(ValueError, match="Time is invalid"):
        convert("0 AM to 8 PM")
    with pytest.raises(ValueError, match="Time is invalid"):
        convert("7:60 AM to 8 PM")
    with pytest.raises(ValueError, match="Time is invalid"):
        convert("13 AM to 8 PM")
    with pytest.raises(ValueError, match="Time is invalid"):
        convert("7 AM to 0 PM")
    with pytest.raises(ValueError, match="Time is invalid"):
        convert("7 AM to 8:75 PM")
    with pytest.raises(ValueError, match="Time is invalid"):
        convert("7 AM to 14 PM")


def test_dummy():
    assert 5 == 5
