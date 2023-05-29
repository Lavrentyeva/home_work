

# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="Vera", middlename="Ivanovna", lastname="Lavrentyeva", nickname="Listopad", title="VVV",
                    company="Romashka",
                    address="qqq", homephone="qqq", mobilephone="1234567", workphone="aaaa", fax="12365498", email="qqq@qq.qq",
                    email2="qqq2@qq.qq", email3="qqq3@qq.qq",
                    homepage="www.www.ww", bday="1", bmonth="January", byear="1999", aday="1", amonth="January",
                    ayear="1999", address2="zzz", secondaryphone="xxx", notes="ccc"))

    old_contact = app.contact.get_contact_list()
    contact = Contact(firstname="Vera1", middlename ="Ivanovna1", lastname="Lavrentyeva1", nickname="Listopad1", title="VVV1", company="Romashka1",
                               address="qqq1", homephone="qqq1", mobilephone="1234567111", workphone ="aaaa1", fax="12365498111", email="qqq1@qq.qq", email2="qqq12@qq.qq", email3="qqq13@qq.qq",
                               homepage="www.www1.ww", bday="11", bmonth="February", byear="1991", aday="11", amonth="February",
                               ayear="1991", address2="zzz1", secondaryphone="xxx1", notes="ccc1")
    contact.id = old_contact[0].id
    app.contact.edit(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[0] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)