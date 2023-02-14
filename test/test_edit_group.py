# -*- coding: utf-8 -*-

from model.group import Group

def test_edit_group(app):
    app.group.edit(Group(name ="zxz1", header ="zxz1", footer ="zxz1"))


