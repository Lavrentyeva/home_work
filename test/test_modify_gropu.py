
from model.group import Group
from random import randrange
import random

def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test", header="", footer=""))
    old_groups = db.get_group_list()
    random_group = random.choice(old_groups)
    group = Group(name="new name")
    id_mod = random_group.id
    #group.id = old_groups.id_mod
    app.group.modify_group_by_id(id_mod, group)
    index = old_groups.index(random_group)
    old_groups[index].name = group.name
    new_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def test_modify_group_header(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test", header="", footer=""))
    old_groups = db.get_group_list()
    random_group = random.choice(old_groups)
    group = Group(header="New header")
    id_mod = random_group.id
    #group.id = old_groups.id_mod
    app.group.modify_group_by_id(id_mod, group)
    index = old_groups.index(random_group)
    old_groups[index].header = group.header
    new_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def test_modify_group_footer(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test", header="", footer=""))
    old_groups = db.get_group_list()
    random_group = random.choice(old_groups)
    group = Group(footer="New footer")
    id_mod = random_group.id
    #group.id = old_groups.id_mod
    app.group.modify_group_by_id(id_mod, group)
    index = old_groups.index(random_group)
    old_groups[index].footer = group.footer
    new_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


