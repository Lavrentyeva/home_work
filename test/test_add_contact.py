# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(user_name="admin", password="secret")
    app.contact.create(Contact(firstname="Vera", middlename ="Ivanovna", lastname="Lavrentyeva", nickname="Listopad", title="VVV", company="Romashka",
                               address="qqq", home="qqq", mobile="1234567", work ="aaaa", fax="12365498", email="qqq@qq.qq", email2="qqq2@qq.qq", email3="qqq3@qq.qq",
                               homepage="www.www.ww", bday="1", bmonth="January", byear="1999", aday="1", amonth="January",
                               ayear="1999", address2="zzz", phone2="xxx", notes="ccc"))
    app.session.logout()

