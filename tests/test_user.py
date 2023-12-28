from helio_main import User


def test_return_with_normalize():
    text = 'Ação'
    user = User(information=text)
    user.normalize()

    assert user.information == 'acao'


def test_return_normalize_lower():
    text = 'TÉRMINO'
    user = User(information=text)
    user.normalize()

    assert user.information.islower()


def test_return_without_accentuation():
    text = 'bênção'
    user = User(information=text)
    user.normalize()

    assert user.information != text


def test_valid_len_information():
    text = 'testing'
    num = 20
    user = User(information=text, limit=num)

    assert user.is_valid_information()


def test_invalid_len_information():
    text = 'testing' 
    num = 5
    user = User(information=text, limit=num)

    assert not user.is_valid_information()