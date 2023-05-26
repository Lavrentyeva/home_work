
from model.contact import Contact
def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="Vera", middlename="Ivanovna", lastname="Lavrentyeva", nickname="Listopad", title="VVV",
                    company="Romashka",
                    address="qqq", home="qqq", mobile="1234567", work="aaaa", fax="12365498", email="qqq@qq.qq",
                    email2="qqq2@qq.qq", email3="qqq3@qq.qq",
                    homepage="www.www.ww", bday="1", bmonth="January", byear="1999", aday="1", amonth="January",
                    ayear="1999", address2="zzz", phone2="xxx", notes="ccc"))
    old_contact = app.contact.get_contact_list()
    contact = Contact(firstname="New firstname")
    contact.id = old_contact[0].id
    app.contact.modify_first_contact(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[0] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)

def test_modify_contact_middlename(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="Vera", middlename="Ivanovna", lastname="Lavrentyeva", nickname="Listopad", title="VVV",
                    company="Romashka",
                    address="qqq", home="qqq", mobile="1234567", work="aaaa", fax="12365498", email="qqq@qq.qq",
                    email2="qqq2@qq.qq", email3="qqq3@qq.qq",
                    homepage="www.www.ww", bday="1", bmonth="January", byear="1999", aday="1", amonth="January",
                    ayear="1999", address2="zzz", phone2="xxx", notes="ccc"))
    old_contact = app.contact.get_contact_list()
    contact = Contact(middlename="New middlename")
    contact.id = old_contact[0].id
    app.contact.modify_first_contact(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[0] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


def test_modify_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="Vera", middlename="Ivanovna", lastname="Lavrentyeva", nickname="Listopad", title="VVV",
                    company="Romashka",
                    address="qqq", home="qqq", mobile="1234567", work="aaaa", fax="12365498", email="qqq@qq.qq",
                    email2="qqq2@qq.qq", email3="qqq3@qq.qq",
                    homepage="www.www.ww", bday="1", bmonth="January", byear="1999", aday="1", amonth="January",
                    ayear="1999", address2="zzz", phone2="xxx", notes="ccc"))

    old_contact = app.contact.get_contact_list()
    contact = Contact(lastname="New lastname")
    contact.id = old_contact[0].id
    app.contact.modify_first_contact(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[0] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


def test_modify_contact_nickname(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="Vera", middlename="Ivanovna", lastname="Lavrentyeva", nickname="Listopad", title="VVV",
                    company="Romashka",
                    address="qqq", home="qqq", mobile="1234567", work="aaaa", fax="12365498", email="qqq@qq.qq",
                    email2="qqq2@qq.qq", email3="qqq3@qq.qq",
                    homepage="www.www.ww", bday="1", bmonth="January", byear="1999", aday="1", amonth="January",
                    ayear="1999", address2="zzz", phone2="xxx", notes="ccc"))

    old_contact = app.contact.get_contact_list()
    contact = Contact(nickname="New nickname")
    contact.id = old_contact[0].id
    app.contact.modify_first_contact(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[0] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)

def test_modify_contact_title(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="Vera", middlename="Ivanovna", lastname="Lavrentyeva", nickname="Listopad", title="VVV",
                    company="Romashka",
                    address="qqq", home="qqq", mobile="1234567", work="aaaa", fax="12365498", email="qqq@qq.qq",
                    email2="qqq2@qq.qq", email3="qqq3@qq.qq",
                    homepage="www.www.ww", bday="1", bmonth="January", byear="1999", aday="1", amonth="January",
                    ayear="1999", address2="zzz", phone2="xxx", notes="ccc"))

    old_contact = app.contact.get_contact_list()
    contact = Contact(title="New title")
    contact.id = old_contact[0].id
    app.contact.modify_first_contact(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[0] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


def test_modify_contact_company(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="Vera", middlename="Ivanovna", lastname="Lavrentyeva", nickname="Listopad", title="VVV",
                    company="Romashka",
                    address="qqq", home="qqq", mobile="1234567", work="aaaa", fax="12365498", email="qqq@qq.qq",
                    email2="qqq2@qq.qq", email3="qqq3@qq.qq",
                    homepage="www.www.ww", bday="1", bmonth="January", byear="1999", aday="1", amonth="January",
                    ayear="1999", address2="zzz", phone2="xxx", notes="ccc"))

    old_contact = app.contact.get_contact_list()
    contact = Contact(company="New company")
    contact.id = old_contact[0].id
    app.contact.modify_first_contact(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[0] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


def test_modify_contact_address(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="Vera", middlename="Ivanovna", lastname="Lavrentyeva", nickname="Listopad", title="VVV",
                    company="Romashka",
                    address="qqq", home="qqq", mobile="1234567", work="aaaa", fax="12365498", email="qqq@qq.qq",
                    email2="qqq2@qq.qq", email3="qqq3@qq.qq",
                    homepage="www.www.ww", bday="1", bmonth="January", byear="1999", aday="1", amonth="January",
                    ayear="1999", address2="zzz", phone2="xxx", notes="ccc"))

    old_contact = app.contact.get_contact_list()
    contact = Contact(address="New address")
    contact.id = old_contact[0].id
    app.contact.modify_first_contact(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[0] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)

def test_modify_contact_home(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="Vera", middlename="Ivanovna", lastname="Lavrentyeva", nickname="Listopad", title="VVV",
                    company="Romashka",
                    address="qqq", home="qqq", mobile="1234567", work="aaaa", fax="12365498", email="qqq@qq.qq",
                    email2="qqq2@qq.qq", email3="qqq3@qq.qq",
                    homepage="www.www.ww", bday="1", bmonth="January", byear="1999", aday="1", amonth="January",
                    ayear="1999", address2="zzz", phone2="xxx", notes="ccc"))

    old_contact = app.contact.get_contact_list()
    contact = Contact(home="New home")
    contact.id = old_contact[0].id
    app.contact.modify_first_contact(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[0] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


def test_modify_contact_mobile(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="Vera", middlename="Ivanovna", lastname="Lavrentyeva", nickname="Listopad", title="VVV",
                    company="Romashka",
                    address="qqq", home="qqq", mobile="1234567", work="aaaa", fax="12365498", email="qqq@qq.qq",
                    email2="qqq2@qq.qq", email3="qqq3@qq.qq",
                    homepage="www.www.ww", bday="1", bmonth="January", byear="1999", aday="1", amonth="January",
                    ayear="1999", address2="zzz", phone2="xxx", notes="ccc"))

    old_contact = app.contact.get_contact_list()
    contact = Contact(mobile="New mobile")
    contact.id = old_contact[0].id
    app.contact.modify_first_contact(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[0] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


def test_modify_contact_work(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="Vera", middlename="Ivanovna", lastname="Lavrentyeva", nickname="Listopad", title="VVV",
                    company="Romashka",
                    address="qqq", home="qqq", mobile="1234567", work="aaaa", fax="12365498", email="qqq@qq.qq",
                    email2="qqq2@qq.qq", email3="qqq3@qq.qq",
                    homepage="www.www.ww", bday="1", bmonth="January", byear="1999", aday="1", amonth="January",
                    ayear="1999", address2="zzz", phone2="xxx", notes="ccc"))

    old_contact = app.contact.get_contact_list()
    contact = Contact(work="New work")
    contact.id = old_contact[0].id
    app.contact.modify_first_contact(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[0] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


def test_modify_contact_fax(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="Vera", middlename="Ivanovna", lastname="Lavrentyeva", nickname="Listopad", title="VVV",
                    company="Romashka",
                    address="qqq", home="qqq", mobile="1234567", work="aaaa", fax="12365498", email="qqq@qq.qq",
                    email2="qqq2@qq.qq", email3="qqq3@qq.qq",
                    homepage="www.www.ww", bday="1", bmonth="January", byear="1999", aday="1", amonth="January",
                    ayear="1999", address2="zzz", phone2="xxx", notes="ccc"))

    old_contact = app.contact.get_contact_list()
    contact = Contact(fax="New fax")
    contact.id = old_contact[0].id
    app.contact.modify_first_contact(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[0] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


def test_modify_contact_email(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="Vera", middlename="Ivanovna", lastname="Lavrentyeva", nickname="Listopad", title="VVV",
                    company="Romashka",
                    address="qqq", home="qqq", mobile="1234567", work="aaaa", fax="12365498", email="qqq@qq.qq",
                    email2="qqq2@qq.qq", email3="qqq3@qq.qq",
                    homepage="www.www.ww", bday="1", bmonth="January", byear="1999", aday="1", amonth="January",
                    ayear="1999", address2="zzz", phone2="xxx", notes="ccc"))

    old_contact = app.contact.get_contact_list()
    contact = Contact(email="qqq1@qq.qq")
    contact.id = old_contact[0].id
    app.contact.modify_first_contact(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[0] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)



def test_modify_contact_email2(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="Vera", middlename="Ivanovna", lastname="Lavrentyeva", nickname="Listopad", title="VVV",
                    company="Romashka",
                    address="qqq", home="qqq", mobile="1234567", work="aaaa", fax="12365498", email="qqq@qq.qq",
                    email2="qqq2@qq.qq", email3="qqq3@qq.qq",
                    homepage="www.www.ww", bday="1", bmonth="January", byear="1999", aday="1", amonth="January",
                    ayear="1999", address2="zzz", phone2="xxx", notes="ccc"))

    old_contact = app.contact.get_contact_list()
    contact = Contact(email2="qqq12@qq.qq")
    contact.id = old_contact[0].id
    app.contact.modify_first_contact(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[0] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


def test_modify_contact_email3(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="Vera", middlename="Ivanovna", lastname="Lavrentyeva", nickname="Listopad", title="VVV",
                    company="Romashka",
                    address="qqq", home="qqq", mobile="1234567", work="aaaa", fax="12365498", email="qqq@qq.qq",
                    email2="qqq2@qq.qq", email3="qqq3@qq.qq",
                    homepage="www.www.ww", bday="1", bmonth="January", byear="1999", aday="1", amonth="January",
                    ayear="1999", address2="zzz", phone2="xxx", notes="ccc"))

    old_contact = app.contact.get_contact_list()
    contact = Contact(email3="qqq13@qq.qq")
    contact.id = old_contact[0].id
    app.contact.modify_first_contact(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[0] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)

def test_modify_contact_homepage(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="Vera", middlename="Ivanovna", lastname="Lavrentyeva", nickname="Listopad", title="VVV",
                    company="Romashka",
                    address="qqq", home="qqq", mobile="1234567", work="aaaa", fax="12365498", email="qqq@qq.qq",
                    email2="qqq2@qq.qq", email3="qqq3@qq.qq",
                    homepage="www.www.ww", bday="1", bmonth="January", byear="1999", aday="1", amonth="January",
                    ayear="1999", address2="zzz", phone2="xxx", notes="ccc"))

    old_contact = app.contact.get_contact_list()
    contact = Contact(homepage="www.www1.ww")
    contact.id = old_contact[0].id
    app.contact.modify_first_contact(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[0] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)

def test_modify_contact_bday(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="Vera", middlename="Ivanovna", lastname="Lavrentyeva", nickname="Listopad", title="VVV",
                    company="Romashka",
                    address="qqq", home="qqq", mobile="1234567", work="aaaa", fax="12365498", email="qqq@qq.qq",
                    email2="qqq2@qq.qq", email3="qqq3@qq.qq",
                    homepage="www.www.ww", bday="1", bmonth="January", byear="1999", aday="1", amonth="January",
                    ayear="1999", address2="zzz", phone2="xxx", notes="ccc"))

    old_contact = app.contact.get_contact_list()
    contact = Contact(bday="11")
    contact.id = old_contact[0].id
    app.contact.modify_first_contact(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[0] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


def test_modify_contact_bmonth(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="Vera", middlename="Ivanovna", lastname="Lavrentyeva", nickname="Listopad", title="VVV",
                    company="Romashka",
                    address="qqq", home="qqq", mobile="1234567", work="aaaa", fax="12365498", email="qqq@qq.qq",
                    email2="qqq2@qq.qq", email3="qqq3@qq.qq",
                    homepage="www.www.ww", bday="1", bmonth="January", byear="1999", aday="1", amonth="January",
                    ayear="1999", address2="zzz", phone2="xxx", notes="ccc"))

    old_contact = app.contact.get_contact_list()
    contact = Contact(bmonth="February")
    contact.id = old_contact[0].id
    app.contact.modify_first_contact(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[0] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)

def test_modify_contact_byear(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="Vera", middlename="Ivanovna", lastname="Lavrentyeva", nickname="Listopad", title="VVV",
                    company="Romashka",
                    address="qqq", home="qqq", mobile="1234567", work="aaaa", fax="12365498", email="qqq@qq.qq",
                    email2="qqq2@qq.qq", email3="qqq3@qq.qq",
                    homepage="www.www.ww", bday="1", bmonth="January", byear="1999", aday="1", amonth="January",
                    ayear="1999", address2="zzz", phone2="xxx", notes="ccc"))

    old_contact = app.contact.get_contact_list()
    contact = Contact(byear="1991")
    contact.id = old_contact[0].id
    app.contact.modify_first_contact(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[0] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)

def test_modify_contact_aday(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="Vera", middlename="Ivanovna", lastname="Lavrentyeva", nickname="Listopad", title="VVV",
                    company="Romashka",
                    address="qqq", home="qqq", mobile="1234567", work="aaaa", fax="12365498", email="qqq@qq.qq",
                    email2="qqq2@qq.qq", email3="qqq3@qq.qq",
                    homepage="www.www.ww", bday="1", bmonth="January", byear="1999", aday="1", amonth="January",
                    ayear="1999", address2="zzz", phone2="xxx", notes="ccc"))

    old_contact = app.contact.get_contact_list()
    contact = Contact(aday="11")
    contact.id = old_contact[0].id
    app.contact.modify_first_contact(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[0] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


def test_modify_contact_amonth(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="Vera", middlename="Ivanovna", lastname="Lavrentyeva", nickname="Listopad", title="VVV",
                    company="Romashka",
                    address="qqq", home="qqq", mobile="1234567", work="aaaa", fax="12365498", email="qqq@qq.qq",
                    email2="qqq2@qq.qq", email3="qqq3@qq.qq",
                    homepage="www.www.ww", bday="1", bmonth="January", byear="1999", aday="1", amonth="January",
                    ayear="1999", address2="zzz", phone2="xxx", notes="ccc"))

    old_contact = app.contact.get_contact_list()
    contact = Contact(amonth="February")
    contact.id = old_contact[0].id
    app.contact.modify_first_contact(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[0] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)

def test_modify_contact_ayear(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="Vera", middlename="Ivanovna", lastname="Lavrentyeva", nickname="Listopad", title="VVV",
                    company="Romashka",
                    address="qqq", home="qqq", mobile="1234567", work="aaaa", fax="12365498", email="qqq@qq.qq",
                    email2="qqq2@qq.qq", email3="qqq3@qq.qq",
                    homepage="www.www.ww", bday="1", bmonth="January", byear="1999", aday="1", amonth="January",
                    ayear="1999", address2="zzz", phone2="xxx", notes="ccc"))

    old_contact = app.contact.get_contact_list()
    contact = Contact(ayear="1991")
    contact.id = old_contact[0].id
    app.contact.modify_first_contact(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[0] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


def test_modify_contact_address2(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="Vera", middlename="Ivanovna", lastname="Lavrentyeva", nickname="Listopad", title="VVV",
                    company="Romashka",
                    address="qqq", home="qqq", mobile="1234567", work="aaaa", fax="12365498", email="qqq@qq.qq",
                    email2="qqq2@qq.qq", email3="qqq3@qq.qq",
                    homepage="www.www.ww", bday="1", bmonth="January", byear="1999", aday="1", amonth="January",
                    ayear="1999", address2="zzz", phone2="xxx", notes="ccc"))

    old_contact = app.contact.get_contact_list()
    contact = Contact(address2="New address2")
    contact.id = old_contact[0].id
    app.contact.modify_first_contact(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[0] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


def test_modify_contact_phone2(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="Vera", middlename="Ivanovna", lastname="Lavrentyeva", nickname="Listopad", title="VVV",
                    company="Romashka",
                    address="qqq", home="qqq", mobile="1234567", work="aaaa", fax="12365498", email="qqq@qq.qq",
                    email2="qqq2@qq.qq", email3="qqq3@qq.qq",
                    homepage="www.www.ww", bday="1", bmonth="January", byear="1999", aday="1", amonth="January",
                    ayear="1999", address2="zzz", phone2="xxx", notes="ccc"))

    old_contact = app.contact.get_contact_list()
    contact = Contact(phone2="New phone2")
    contact.id = old_contact[0].id
    app.contact.modify_first_contact(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[0] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


def test_modify_contact_notes(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="Vera", middlename="Ivanovna", lastname="Lavrentyeva", nickname="Listopad", title="VVV",
                    company="Romashka",
                    address="qqq", home="qqq", mobile="1234567", work="aaaa", fax="12365498", email="qqq@qq.qq",
                    email2="qqq2@qq.qq", email3="qqq3@qq.qq",
                    homepage="www.www.ww", bday="1", bmonth="January", byear="1999", aday="1", amonth="January",
                    ayear="1999", address2="zzz", phone2="xxx", notes="ccc"))

    old_contact = app.contact.get_contact_list()
    contact = Contact(notes="New notes")
    contact.id = old_contact[0].id
    app.contact.modify_first_contact(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[0] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)

