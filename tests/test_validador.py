""" Module containing unit tests for the Validador class in helio module."""
from helio import Validator


def test_str_normalize_lower():
    """Test the string lower after normalize."""
    text = "ABCDEFG"
    result = Validator().normalize(text)

    assert result.islower()


def test_str_normalize_without_accentuation():
    """Test the string without accentuation."""
    text = "ãêíõù"
    result = Validator().normalize(text)

    assert text != result
