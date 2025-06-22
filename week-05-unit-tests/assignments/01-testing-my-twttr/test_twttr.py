from twttr import shorten


def test_without_vowels():
    assert shorten("xyz") == "xyz"
    assert shorten("DVD-RW") == "DVD-RW"
    assert shorten("256 GB SSD") == "256 GB SSD"
    assert shorten("   PV  =  n * R * T  ") == "   PV  =  n * R * T  "


def test_with_vowels():
    assert shorten("hello") == "hll"
    assert shorten("banana leaves") == "bnn lvs"
    assert shorten("  Twitter PaGe  ") == "  Twttr PG  "


def test_with_uppercase_vowels():
    assert shorten("Undefined") == "ndfnd"
    assert shorten("I study at IIIT Allahabad") == " stdy t T llhbd"


def test_with_punctuation():
    assert shorten("What's your name?") == "Wht's yr nm?"
