from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("hello, David") == 0
    assert value("Hello!! Good afternoon") == 0


def test_nonhello_startswith_h():
    assert value("howdy?") == 20
    assert value("hmu, ok?") == 20
    assert value("Heck, naw!") == 20


def test_nonhello():
    assert value("wait in the queue") == 100
    assert value("Lunch time - get lost!") == 100
    assert value("Fill the form") == 100
