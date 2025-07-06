from um import count


def test_mixed_case():
    assert count("Um what?") == 1
    assert count("uM, excuse me?") == 1
    assert count("UM... I forgot.") == 1


def test_beginning_str():
    assert count("um, hello there") == 1
    assert count("Um, um, um, this is many") == 3
    assert count("um") == 1


def test_ending_str():
    assert count("hello um") == 1
    assert count("This is many, um, um, um") == 3
    assert count("hello um.") == 1


def test_mid_str():
    assert count("hello, um, world") == 1
    assert count("one, um, two, um, three") == 2
    assert count("what, um, next") == 1


def test_with_special_chars():
    assert count("um...") == 1
    assert count("um?") == 1
    assert count("um,") == 1
    assert count("um!") == 1
    assert count("Um - yeah") == 1
    assert count("What, um... okay.") == 1


def test_within_words():
    assert count("yummy") == 0
    assert count("umbrella") == 0
    assert count("maximum") == 0
    assert count("forum") == 0
    assert count("dummy text") == 0
    assert count("chromium um") == 1
