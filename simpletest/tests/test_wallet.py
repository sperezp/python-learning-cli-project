import pytest
from simpletest.wallet import Wallet, InsufficientAmount


@pytest.fixture
def empty_wallet():
    """Return a Wallet instance with a zero balance"""
    return Wallet()


@pytest.fixture
def wallet():
    """Return a Wallet instance with a balance of 20"""
    return Wallet(20)


def test_default_initial_amount(empty_wallet):
    assert empty_wallet.balance == 0


def test_setting_initial_amount(wallet):
    assert wallet.balance == 20


def test_add_cash(wallet):
    wallet.add_cash(3)
    assert wallet.balance == 23


def test_spend_cash(wallet):
    wallet.spend_cash(3)
    assert wallet.balance == 17


def test_spend_cash_with_insufficient_balance(empty_wallet):
    with pytest.raises(InsufficientAmount):
        empty_wallet.spend_cash(3)


@pytest.mark.parametrize("earned, spent, expected", [
    (30, 10, 20),
    (20, 2, 18),
    (45, 8, 37)
])
def test_transactions(empty_wallet, earned, spent, expected):
    my_wallet = empty_wallet
    my_wallet.add_cash(earned)
    my_wallet.spend_cash(spent)
    assert my_wallet.balance == expected
