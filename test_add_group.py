# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from application import Application
from group import Group
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(user_name="admin", password="secret")
    app.create_group(Group(name = "zxz", header = "zxz",footer = "zxz"))
    app.logout()


def test_add_empty_group(app):
    app.login(user_name="admin", password="secret")
    app.create_group(Group(name = "", header = "",footer = ""))
    app.logout()


