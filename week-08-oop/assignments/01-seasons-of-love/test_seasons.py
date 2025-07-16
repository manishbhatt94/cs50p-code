from datetime import date

import pytest
from seasons import get_message, parse_iso_date_str


def test_parse_iso_date_str_invalid_format():
    with pytest.raises(ValueError):
        parse_iso_date_str("1 January 1999")
    with pytest.raises(ValueError):
        parse_iso_date_str("25 Feb 2004")
    with pytest.raises(ValueError):
        parse_iso_date_str("31/03/2005")


def test_parse_iso_date_str_invalid_date():
    with pytest.raises(ValueError):
        parse_iso_date_str("1999-01-35")
    with pytest.raises(ValueError):
        parse_iso_date_str("2025-02-29")
    with pytest.raises(ValueError):
        parse_iso_date_str("2010-14-31")


def test_get_message_dob_after_today():
    with pytest.raises(ValueError):
        get_message(
            from_date=date.fromisoformat("2025-12-31"),
            to_date=date.fromisoformat("2025-12-30"),
        )
    with pytest.raises(ValueError):
        get_message(
            from_date=date.fromisoformat("2021-01-01"),
            to_date=date.fromisoformat("2020-12-31"),
        )


def test_get_message_return():
    assert (  # one year
        get_message(
            from_date=date.fromisoformat("2021-01-01"),
            to_date=date.fromisoformat("2022-01-01"),
        )
        == "Five hundred twenty-five thousand, six hundred minutes"
    )
    assert (  # one year - includes leap year extra day
        get_message(
            from_date=date.fromisoformat("2024-02-20"),
            to_date=date.fromisoformat("2025-02-20"),
        )
        == "Five hundred twenty-seven thousand forty minutes"
    )
    assert (  # two years
        get_message(
            from_date=date.fromisoformat("2021-01-01"),
            to_date=date.fromisoformat("2023-01-01"),
        )
        == "One million, fifty-one thousand, two hundred minutes"
    )
    assert (  # two years - includes leap year extra day
        get_message(
            from_date=date.fromisoformat("2023-01-15"),
            to_date=date.fromisoformat("2025-01-15"),
        )
        == "One million, fifty-two thousand, six hundred forty minutes"
    )
    assert (  # one day
        get_message(
            from_date=date.fromisoformat("2024-12-31"),
            to_date=date.fromisoformat("2025-01-01"),
        )
        == "One thousand, four hundred forty minutes"
    )
    assert (  # thirty years
        get_message(
            from_date=date.fromisoformat("1970-01-01"),
            to_date=date.fromisoformat("2000-01-01"),
        )
        == "Fifteen million, seven hundred seventy-eight thousand eighty minutes"
    )
