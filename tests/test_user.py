""" Module containing unit tests for the User class in helio module."""
from helio import User


def test_return_with_normalize():
    """
    Test if the User class normalizes the input text
    by removing accents and converting to lowercase.
    """
    text = "Ação"
    user = User(information=text)
    user.normalize()

    assert user.information == "acao"


def test_return_normalize_lower():
    """
    Test if the normalized User information is in lowercase.
    """
    text = "TÉRMINO"
    user = User(information=text)
    user.normalize()

    assert user.information.islower()


def test_return_without_accentuation():
    """
    Test if the User class removes accentuations during normalization.
    """
    text = "bênção"
    user = User(information=text)
    user.normalize()

    assert user.information != text


def test_valid_len_information():
    """
    Test if the User class correctly validates information
    length within the specified limit.
    """
    text = "testing"
    num = 20
    user = User(information=text, limit=num)

    assert user.is_valid_information()


def test_invalid_len_information():
    """
    Test if the User class correctly identifies
    invalid information length beyond the specified limit.
    """
    text = "testing"
    num = 5
    user = User(information=text, limit=num)

    assert not user.is_valid_information()
