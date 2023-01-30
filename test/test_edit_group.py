# -*- coding: utf-8 -*-

from model.group import Group

def test_add_group(app):
    app.session.login(user_name="admin", password="secret")
    app.group.edit(Group(name ="zxz1", header ="zxz1", footer ="zxz1"))
    app.session.logout()


