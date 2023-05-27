from model.contact import Contact
def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="Vera", middlename="Ivanovna", lastname="Lavrentyeva", nickname="Listopad", title="VVV",
                    company="Romashka",
                    address="qqq", home="qqq", mobile="1234567", work="aaaa", fax="12365498", email="qqq@qq.qq",
                    email2="qqq2@qq.qq", email3="qqq3@qq.qq",
                    homepage="www.www.ww", bday="1", bmonth="January", byear="1999", aday="1", amonth="January",
                    ayear="1999", address2="zzz", phone2="xxx", notes="ccc"))
    old_contacts = app.contact.get_contact_list()
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts