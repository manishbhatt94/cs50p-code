from plates import is_valid


def test_length():
    # Less than 2 chars - invalid
    assert not is_valid("")
    assert not is_valid("H")
    # Valid length - 2 to 6 chars
    assert is_valid("HE")
    assert is_valid("HEL")
    assert is_valid("HELL")
    assert is_valid("HELLO")
    assert is_valid("HELLOW")
    # More than 6 chars - invalid
    assert not is_valid("HELLOWY")
    assert not is_valid("HELLOWYZ")


def test_leading_two_letters():
    assert is_valid("AB")
    assert not is_valid("A1")
    assert not is_valid("12")


def test_first_digit_nonzero():
    assert not is_valid("abc012")
    assert is_valid("abc102")
    assert is_valid("abc123")


def test_numbers_at_end():
    assert not is_valid("AB12CD")
    assert not is_valid("AB12C3")
    assert is_valid("AB123")


def test_no_special_chars():
    assert not is_valid("  ABCD")
    assert not is_valid("AB CD")
    assert not is_valid("AB.CD")
    assert not is_valid("AB,45")
    assert not is_valid("AB?45")
