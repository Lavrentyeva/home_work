

# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    app.contact.edit(Contact(firstname="Vera1", middlename ="Ivanovna1", lastname="Lavrentyeva1", nickname="Listopad1", title="VVV1", company="Romashka1",
                               address="qqq1", home="qqq1", mobile="1234567111", work ="aaaa1", fax="12365498111", email="qqq1@qq.qq", email2="qqq12@qq.qq", email3="qqq13@qq.qq",
                               homepage="www.www1.ww", bday="11", bmonth="February", byear="1991", aday="11", amonth="February",
                               ayear="1991", address2="zzz1", phone2="xxx1", notes="ccc1"))

