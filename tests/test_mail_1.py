import pytest


@pytest.fixture()
def set_up():
    print("enter systems is Ok")


def test_send_mail_1(set_up):
    print("ok mail-1 send")


def test_send_mail_2(set_up):
    print("ok mail-2 send")




