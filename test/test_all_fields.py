import re
from random import randrange
from model.contact import Contact

def test_comparison_random_home_page_and_edit_page_fields(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="Vera", middlename="Ivanovna", lastname="Lavrentyeva", nickname="Listopad", title="VVV",
                    company="Romashka",
                    address="qqq", homephone="qqq", mobilephone="1234567", workphone="aaaa", fax="12365498",
                    email="qqq@qq.qq",
                    email2="qqq2@qq.qq", email3="qqq3@qq.qq",
                    homepage="www.www.ww", bday="1", bmonth="January", byear="1999", aday="1", amonth="January",
                    ayear="1999", address2="zzz", secondaryphone="xxx", notes="ccc"))

    contact_from_home_page = app.contact.get_contact_list()
    random = randrange(len(contact_from_home_page))
    contact_from_home_page_by_index = app.contact.get_contact_list()[random]
    contact_from_edit_page_by_index = app.contact.get_contact_info_from_edit_page(random)
    assert contact_from_home_page_by_index.firstname == contact_from_edit_page_by_index.firstname
    assert contact_from_home_page_by_index.lastname == contact_from_edit_page_by_index.lastname
    assert contact_from_home_page_by_index.address == contact_from_edit_page_by_index.address
    assert contact_from_home_page_by_index.all_phones_from_home_page == merge_pones_like_on_home_page(contact_from_edit_page_by_index)
    assert contact_from_home_page_by_index.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page_by_index)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_pones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x!="",
                             map(lambda x: clear(x),
                                 filter(lambda x: x is not None,
                                        [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x!="",
                             filter(lambda x: x is not None,
                                   [contact.email, contact.email2, contact.email3])))