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
