# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Vera", middlename ="Ivanovna", lastname="Lavrentyeva", nickname="Listopad", title="VVV", company="Romashka",
                               address="qqq", home="qqq", mobile="1234567", work ="aaaa", fax="12365498", email="qqq@qq.qq", email2="qqq2@qq.qq", email3="qqq3@qq.qq",
                               homepage="www.www.ww", bday="1", bmonth="January", byear="1999", aday="1", amonth="January",
                               ayear="1999", address2="zzz", phone2="xxx", notes="ccc")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
