from numb3rs import validate


def test_happy():
    assert validate("0.0.0.0") is True
    assert validate("1.2.3.4") is True
    assert validate("127.0.0.1") is True
    assert validate("127.0.0.1") is True
    assert validate("255.255.255.0") is True
    assert validate("255.255.255.255") is True


def test_letters():
    assert validate("cat") is False
    assert validate("mary.had") is False
    assert validate("mary.had.a") is False
    assert validate("mary.had.a.little") is False
    assert validate("12a.13b.14c.15d") is False


def test_spaces():
    assert validate(" 192.168.0.1 ") is False
    assert validate("192.168.0.1 ") is False
    assert validate("192 .168.0.1") is False
    assert validate("192. 168.0.1") is False
    assert validate("192.168 .0.1") is False
    assert validate("192.168. 0.1") is False
    assert validate("192.168.0 .1") is False
    assert validate("192.168.0. 1") is False
    # assert validate("192.168.0.1\n") is False


def test_special_chars():
    assert validate("172_13.255.68") is False
    assert validate("172.13?255.68") is False
    assert validate("172.13.255#68") is False
    assert validate("-172.13.255.68") is False
    assert validate("+172.13.255.68") is False


def test_leading_zeroes():
    assert validate("00.168.1.1") is False
    assert validate("000.168.1.1") is False
    assert validate("192.168.001.1") is False
    assert validate("0234.78.196.65") is False
    assert validate("034.78.196.65") is False
    assert validate("34.078.196.65") is False
    assert validate("34.78.0196.65") is False
    assert validate("34.78.096.65") is False
    assert validate("34.78.196.065") is False
    assert validate("0xb3.78.196.65") is False
    assert validate("0x34.78.196.65") is False
    assert validate("34.0x78.196.65") is False
    assert validate("34.78.0x196.65") is False
    assert validate("34.78.0x96.65") is False
    assert validate("34.78.196.0x65") is False


def test_exact_match():
    assert validate("My IP is 172.32.83.12") is False
    assert validate("172.32.83.12 is my static IP.") is False
    assert validate("How did you buy 172.32.83.12 as a static IP?") is False


def test_range():
    assert validate("512.512.512.512") is False
    assert validate("1.2.3.1000") is False
    assert validate("1.2.3.256") is False
    assert validate("256.256.256.256") is False


def test_octets_count():
    assert validate("192") is False
    assert validate("192.168") is False
    assert validate("192.168.12") is False
    assert validate("192.168.12.65") is True  # 4 octets - valid
    assert validate("192.168.12.65.145") is False
    assert validate("192.168.12.65.145.96") is False
