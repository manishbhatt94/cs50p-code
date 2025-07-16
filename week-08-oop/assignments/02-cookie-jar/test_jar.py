import pytest
from jar import Jar


def test_init():
    jar1 = Jar()
    assert jar1.capacity == 12
    assert jar1.size == 0

    jar2 = Jar(capacity=2)
    assert jar2.capacity == 2
    assert jar2.size == 0

    jar3 = Jar(capacity=0)
    assert jar3.capacity == 0
    assert jar3.size == 0

    with pytest.raises(ValueError, match="capacity must be a non-negative int"):
        Jar(capacity=-1)

    with pytest.raises(ValueError, match="capacity must be a non-negative int"):
        Jar(capacity=1.25)

    with pytest.raises(ValueError, match="capacity must be a non-negative int"):
        Jar(capacity="10")

    with pytest.raises(ValueError, match="capacity must be a non-negative int"):
        Jar(capacity="cat")


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar1 = Jar(capacity=10)
    jar1.deposit(2)
    assert jar1.size == 2
    jar1.deposit(5)
    assert jar1.size == 7
    jar1.deposit(3)
    assert jar1.size == 10

    jar2 = Jar(capacity=5)
    jar2.deposit(4)
    with pytest.raises(ValueError, match="size value invalid"):
        jar2.deposit(2)


def test_withdraw():
    jar1 = Jar(capacity=8)
    jar1.size = 8
    jar1.withdraw(5)
    assert jar1.size == 3
    jar1.withdraw(3)
    assert jar1.size == 0

    jar2 = Jar(capacity=6)
    jar2.size = 6
    jar2.withdraw(3)
    with pytest.raises(ValueError, match="size value invalid"):
        jar2.withdraw(4)
